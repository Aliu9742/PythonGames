
#fnding nth prime number, if the nth prime number is beyond my list of prime numbers stored in primeNum (ie: 7th prime number), then generate the prime number until the length of primeNum is equal to n
#generate the next prime number by testing the number 2 above the previous prime number to see if it has any factors
#if it has factors add 2 and test the next number for factors
#repeat this until a new number is generated, the length of primeNum increases by 1 

def nthPrimeNum(n):
  primeNum = [2,3,5,7,11,13]
  while len(primeNum) < n:
    currentNumPrimes = len(primeNum)
    #print("there are", currentNumPrimes, "prime numbers")
    x = primeNum[-1]
    #print("the last known prime number is", x)
    x = x + 2
    #print("the number being tested is", x)
    while currentNumPrimes == len(primeNum):
      #print("THE CURRENT NUMBER OF PRIMES IS", currentNumPrimes)
      #print("THE CURRENT NUMBER OF KNOWN PRIME NUMBERS IS", len(primeNum))
      for num in primeNum:
        #print(num)
        if x % num == 0:
          #print("THE NUMBER TESTED IS", x)
          #print("found a factor", num)
          break 
        elif num == primeNum[-1]:
          primeNum.append(x)
          #print("found a prime number", x)
          #print("THE CURRENT NUMBER OF PRIMES IS", len(primeNum))
        #print(primeNum)
      x = x + 2 

  print(primeNum[n-1])

nthPrimeNum(10001)