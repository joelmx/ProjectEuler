#!/usr/bin/python

res=0

def getNumbers(num1, num2):
  global res
  #if (num2< 20):
  if (num2 < 4000000):
    fib = num1 + num2
    #print fib
    if ( fib%2 == 0):
      res = res + fib
    getNumbers(num2, fib)
  return 

getNumbers(0,1)
print res 
