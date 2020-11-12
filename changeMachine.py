import math
import numpy as np
class Coin:
  def __init__(self, Cointype, value):
    self.Cointype = Cointype
    self.value = value
  
  def HowManyCoins(self, ChangeAmount):
    numCoins = math.floor(ChangeAmount / self.value)
    return numCoins
  
  def ChangeRemaining(self, ChangeAmount):
    remainder = ChangeAmount % self.value
    return remainder

quarter = Coin("quarter", 25)
dime = Coin("dime",10)
nickel = Coin("nickel", 5)
penny = Coin("penny", 1)

def CoinsToGive(ChangeAmount):
  #ChangeAmount = builtins.input ("How many cents is the change?")
  #ChangeAmount = int(ChangeAmount)
  remainingChange = ChangeAmount
  Coins = np.array([quarter,dime,nickel,penny])
  print("the change is", remainingChange, "cents")

  for typeOfCoin in Coins:
    if remainingChange > 0:
      if typeOfCoin.HowManyCoins(remainingChange) > 0:
        print(typeOfCoin.Cointype, "|", typeOfCoin.HowManyCoins(remainingChange))
        remainingChange = typeOfCoin.ChangeRemaining(remainingChange)

        
  print("------")
  
for x in range(100):
  CoinsToGive(x)