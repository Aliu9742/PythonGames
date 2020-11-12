import numpy as np
import math

def whatAreTheFactors(number):
  factors = []
  i = 0
  for x in range(2, math.ceil(np.sqrt(number))+1):
    if number % x == 0:
      if i == 0 :
        factors.append(int(number/x))      
        factors.append(x)
        i = i + 1
      else: 
        factors.insert(-i, x)
        factors.insert(i, int(number/x))
        i = i + 1
     
  return factors


def largestPrimeNumber(factorsList):
  for factor in factorsList:
    numberOfFactors = []
    for x in range(2, math.ceil(np.sqrt(factor))):
      if factor % x == 0:
        numberOfFactors.append(1)
        numberOfFactors.append(1)
    if len(numberOfFactors) == 0:
      return factor



print(largestPrimeNumber(whatAreTheFactors(600851475143)))