# import the magic random picker
import random


# list of things to pick from
activities_to_do = ['a','b','c']


# find a way to pick something
going_to_do = random.choice(activities_to_do)



# a way to tell the user what to do
print "We can do the following " + str(activities_to_do)
print "We are going to do " + going_to_do

