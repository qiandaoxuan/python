# _*_ coding: utf-8 _*_
import boto3
import os
import sys
import time

def get_latest_build(build_version):
    list_file = 'build_list.txt'
    latest_build = ''
    os.system('dir /b %s > %s' %(build_location, list_file))
    f_list = open(list_file, 'r')
    all_lines = f_list.readlines()
    for eachLine in all_lines:
        if eachLine.find(build_version) >= 0:
            latest_build = eachLine.replace('\n', '')
            break
        else:
            continue
    return latest_build

def wait_volume_available(volume_id):
    waiter = ec2_client.get_waiter('volume_available')
    waiter.wait(VolumeIds=[volume_id])

def wait_instance_status_ok(instance_id):
    waiter = ec2_client.get_waiter('instance_status_ok')
    waiter.wait(InstanceIds=[instance_id])

def wait_image_available(image_id):
    waiter = ec2_client.get_waiter('image_available')
    waiter.wait(ImageIds=[image_id])

def revert_volume(instance, snapshot_name):
    root_device = instance.root_device_name
    zone_available = 'cn-north-1b'
    #回滚volume]
    device_list = instance.block_device_mappings
    if len(device_list):
        root_volume_id =  instance.block_device_mappings[0]['Ebs']['VolumeId']

        #卸掉并删除根device
        print 'detach root volume...'
        instance.detach_volume(VolumeId = root_volume_id, Device = root_device)
        wait_volume_available(root_volume_id)
        print 'delete root volume'
        ec2_client.delete_volume(VolumeId = root_volume_id)

    #根据snapshot创建volume,并将其挂载为根device
    print 'creating volume from snapshot...'
    volume_reverted = ec2.create_volume(SnapshotId = snapshot_name, AvailabilityZone = zone_available)
    wait_volume_available(volume_reverted.volume_id)
    print 'attach the newly created volume %s...' %volume_reverted.volume_id
    volume_reverted.attach_to_instance(InstanceId = instance_id, Device = root_device)

    #启动instance，回滚完成
    print 'starting instance...'
    instance.start()
    wait_instance_status_ok(instance.instance_id)

def install_build(dns, build_location, build_file):
    user = 'centos'
    dns_full = '%s@%s' %(user, dns)
    pscp = r'C:\pscp.exe -i fengru.ppk'
    remote_ssh = r'C:\plink.exe -i fengru.ppk %s' %dns_full

    os.system(r'echo y | %s %s\%s %s:/home/centos' %(pscp, build_location, build_file, dns_full))
    os.system(r'%s sudo service nfs start' %remote_ssh)
    os.system(r'%s sudo chmod 777 %s' %(remote_ssh, build_file))
    os.system(r'%s sudo nohup ./%s --silent > %s' %(remote_ssh, build_file, install_log))

def check_install_status():
    f = open(install_log, 'r')
    log = f.read()
    index = log.find('The Arcserve UDP Agent(Linux) was successfully installed')
    if index == -1:
        print 'install build failed'
        sys.exit(-1)
    else:
        print 'install build succeed'

def create_image(instance_id, image_name):
    new_ami = ec2_client.create_image(InstanceId = instance_id, Name = image_name)
    ami_id = new_ami['ImageId']
    print 'creating new image'
    wait_image_available(ami_id)
    image = ec2.Image(ami_id)
    owner = image.owner_id
#    print 'change ami attribute to public'
#    image.modify_attribute(LaunchPermission={'Add': [{'UserId': owner, 'Group': 'all'}]})

def stop_instance(instance_id):
    print 'stopping instance...'
    instance.stop()
    instance.wait_until_stopped()
    print 'build successful'


region = 'cn-north-1'
instance_id = 'i-d64e626e'
ec2 = boto3.resource('ec2', region)
ec2_client = boto3.client('ec2', region)
instance = ec2.Instance(instance_id)
snapshot_reverted = 'snap-06acce31'
build_location = r'\\rmdm-bldvm-l902\CurrentRelease\CRE_D2D\LD2D_UDP_V6.5'
version_file = r'%s\trigger_ami' %build_location

f_version = open(version_file, 'r')
build_version = f_version.read().replace('\n', '')
print 'build version is %s' %build_version
install_log = r'E:\linux_ami\log\install_%s.log' %build_version

build_file = get_latest_build(build_version)
print 'build file is %s' %build_file
image_name = 'ami_with_%s' %build_file

revert_volume(instance, snapshot_reverted)
dns = instance.public_dns_name
install_build(dns, build_location, build_file)
check_install_status()
create_image(instance_id, image_name)
stop_instance(instance_id)



