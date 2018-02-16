#more variable and Printing

my_name = 'Spencer Atkins'
my_age = 40 #not a lie
my_height = 175 #cms
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
height_inches = 100

print "Let's talk about %s." % my_name
print "He's %d cms tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#1 inch  = 2.54cm
print "If you are %d inches tall, then that makes you %d in cms." % (height_inches, height_inches * 2.54)
