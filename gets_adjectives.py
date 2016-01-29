import random 
import urllib2

adjs = urllib2.urlopen("https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/adjectives.lst").read()
#adjs = ['rockstar', 'musician']

print adjs
print type(adjs)
adjs = adjs.split()
print adjs
#print 'Michael is a ' + random.choice(adjs)
