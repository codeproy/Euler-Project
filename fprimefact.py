# find prime factors of a number
import os
import math
n = 24

a = []

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def isprime(n):
  fact = 2 
  while fact < n:
    if n % fact == 0:
      return False
    fact += 1
  return True

def smallprime(n):

  fact = 2

  prime = True
  
  while fact <  round(n ** 0.5) + 1:
   # print('f1 ', fact)
    if n % fact  == 0:
      if isprime(fact):
        prime = False
        return(fact)
    fact += 1
  if prime: return n
    
    

  
def calcbigprime(n):
 # print(smallprime(n))

  lrg = n / smallprime(n)

  while lrg > 2:
    if isprime(lrg):
      return(lrg)
    else:
      lrg = lrg / smallprime(lrg)

  return(n)

  
 
print(calcbigprime(600851475143))
print(calcbigprime(20))
