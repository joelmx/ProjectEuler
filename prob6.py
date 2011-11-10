#!/usr/bin/python

sumOfSquares=0

def sumOfSq(limit):
  suma = 0
  for i in range(1,limit+1):
    suma = suma + i
  sq = pow(suma, 2)
  return sq

def sqOfSum(limit):
  suma = 0
  for i in range(1,limit+1):
    sqi = pow(i,2)
    suma = suma + sqi
  return suma

def diff(limit):
  d = sumOfSq(limit) - sqOfSum(limit)
  return d

print diff(100)
