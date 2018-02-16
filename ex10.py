#what was that - escape characters

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat  = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

thin_cat = '''I'll do another list:
\t* Star Wars
\t* The Departed
\t* My Fair Lady
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print thin_cat

print "I want to print %r rather than %s." % ("With \"quotes\"", "some more \"quotes\"")
