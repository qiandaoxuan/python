import re

pattern = re.compile(r'world')
str1 = 'hello world!'
str2 = 'i say, hello world!'

print re.match(pattern, str1)
print re.search(pattern, str1).span()

print re.split(r'\d+', 'a1b22vvv4dd32a')

print re.findall(r'\d+', 'a1b22vvv4dd32a')

for i in re.finditer(r'\d+', 'a1b22vvv4dd32a'):
    print i.group()

p = re.compile(r'(\w+) (\w+)')
print p.sub(r'\2 \1', str1)
print p.subn(r'\2 \1', str2)
