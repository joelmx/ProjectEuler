#!/usr/bin/python

mynumber= 13195
mynumber=600851475143L
milista=[]

def esFactor(numero):
  global mynumber
  if (mynumber%numero == 0):
    return True
  return False

def isPrime(number):
  for index in range(2,number-1):
    if ( number%index == 0):
      return False
  return True

def multip():
  global milista
  acum = 1
  for item in milista:
    acum = acum * item
  return acum

cur = 2
while(cur < mynumber):
  #if(cur>10):
    #break
  print "inicia num ", cur
  if ( esFactor(cur) ):
    factor = mynumber/cur
    print "factores: %s y %s"%(cur, factor)
    if( isPrime(cur) ):
      print "factor primo: ", cur 
      milista.append(cur)
      if (mynumber == multip() ):
        print "ganador: ", max(milista)
        break 
  cur = cur + 1

print milista

