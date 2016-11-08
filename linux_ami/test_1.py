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
            latest_build = eachLine
            break
        else:
            continue
    return latest_build

build_location = r'\\rmdm-bldvm-l902\CurrentRelease\CRE_D2D\LD2D_UDP_V6.5'
version_file = r'%s\trigger_ami' %build_location

f_version = open(version_file, 'r')
build_version = f_version.read().replace('\n', '')
print 'build version is %s' %build_version
build_file = get_latest_build(build_version)
print 'build file is %s' %build_file