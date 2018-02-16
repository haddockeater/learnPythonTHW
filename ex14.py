from sys import argv

script, user_name, place = argv
#setting the variable once here, means it can be referenced thorughout the script
#without having to re-type
prompt = ':-> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. But I live in %r.
And you have a %r computer. Nice.
""" % (likes, lives, place, computer)
