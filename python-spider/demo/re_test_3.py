import re

s = '<usr1@mail1> usr2@mail2'
print re.findall(r'(<)?(\w+@\w+)(?(1)>)', s)


