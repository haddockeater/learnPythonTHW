from sys import argv
from os.path import exists

script, from_file, to_file = argv

#ex17.py reduced to one line of code

open(to_file, 'w').write(open(from_file).read())
