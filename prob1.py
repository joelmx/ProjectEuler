#!/usr/bin/python

counter = 1
finalsum = 0
while (counter<1000):
  if ( counter%3 == 0 or counter%5 == 0):
    finalsum = finalsum + counter 
  counter = counter + 1
print finalsum
