#import the input arguments module
from sys import argv

#unpack the input variables, "script" being the name of the python file
script, name, age, colour = argv

#get the users name
yname = raw_input("What is your name?")
#print the users name and the input variable value for name 
print "Your name is %s. My name is %s." % (yname, name)

yage = raw_input("How old are you?")
print "You are %r years old. I am %r." % (yage, age)

ycolour = raw_input("What is your favourite colour?")
print "Your favourite colour is %r. Mine is %r." % (ycolour, colour)
