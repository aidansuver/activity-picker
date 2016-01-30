# import the magic random picker
import random, urllib2


# list of things to pick from
activities_to_do = ['a','b','c']
activities_to_do = urllib2.urlopen('https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/code_activities_we_like.lst').read()


# find a way to pick something
going_to_do = random.choice(activities_to_do)



# a way to tell the user what to do
print "We can do the following " + str(activities_to_do)
print "We are going to do " + going_to_do

debug_example = "DEBUG: showing how it works typing.io\ncodeskulptor\ncodecombat\ncodeacademy\nscratch\nkaggle\ntynker?\n"
print debug_example.split()
