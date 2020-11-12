#Welcome to Battleship! So far, the only thing to do is placing ships of lengths 2-5 on a 8x8 board.
#Next step is having player and bot take turns attacking each other's board, keep track of what ship has been sunk, and knowing when the game ends and declaring the winner

import numpy as np
from numpy import random
import builtins 


class board:

  def __init__(self,whichSide, boardLayout):
    self.whichSide = whichSide
    self.boardLayout = boardLayout
  
  def printBoard(self):
    print ("   0 1 2 3 4 5 6 7")
    
    for x in range(self.boardLayout.shape[0]):
      print(x, self.boardLayout[x], x)
    
    print ("   0 1 2 3 4 5 6 7")
    print("-------------------------")
  
  def target(self):
    #need to deal with bad input
    row = builtins.input("Choose row from 0 to 7:")
    row = int(row)

    column = builtins.input("Choose column from 0 to 7:")
    column = int(column)
    
    self.boardLayout[row][column] = self.boardLayout[row][column] + 2
  
  def posIsNotAllowed(self, posArray):
    
    if posArray[0] > self.boardLayout.shape[0] -1 or posArray[0] < 0 or posArray[1] > self.boardLayout.shape[1] - 1 or posArray[1] < 0:
      return True
    
    elif self.boardLayout[posArray[0]][posArray[1]] > 0:
      return True
    
    return False
  
  
  
  def orientationNotAllowed(self, posArray, shipArray):
    orientationNotAllowed = np.array([0,0,0,0])
    for x in range(len(shipArray)):
      if self.posIsNotAllowed(np.array([posArray[0] -x, posArray[1]])):
        orientationNotAllowed[0] = 1
      if self.posIsNotAllowed(np.array([posArray[0] + x, posArray[1]])):
        orientationNotAllowed[1] = 1
      if self.posIsNotAllowed(np.array([posArray[0], posArray[1] - x])):
        orientationNotAllowed[2] = 1
      if self.posIsNotAllowed(np.array([posArray[0], posArray[1] + x])):
        orientationNotAllowed[3] = 1
    return orientationNotAllowed
  
  def askForPos(self):
    row = 10
    column = 10
    while self.posIsNotAllowed(np.array([row, column])):
      if self.whichSide == 0:
        row = builtins.input("Choose row: ")
        row = int(row)
    
        column = builtins.input("Choose column: ")
        column = int(column)
      
      if self.whichSide == 1:
        row = random.randint(self.boardLayout.shape[0])
        column = random.randint(self.boardLayout.shape[1])
    
    return np.array([row, column])
  
  def makeShipPos(self, shipArray):
    shipPos = self.askForPos()
    while np.all(self.orientationNotAllowed(shipPos, shipArray)):
      shipPos = self.askForPos()
    orientation = 5
    while orientation > 4 or orientation < 0 or self.orientationNotAllowed(shipPos, shipArray)[orientation-1]:
      if self.whichSide == 0:
        orientation = builtins.input("Choose orientation from 1 to 4. 1. up, 2. down, 3. left, 4. right: ")
        orientation = int(orientation)

      if self.whichSide == 1:
        orientation = random.randint(1,5)
  
    shipPosArray = np.array([shipPos[0], shipPos[1], orientation, len(shipArray),shipArray[0]])   
    return shipPosArray


  def placeShip(self, shipPosArray):
    
    if shipPosArray[2] == 1:
      for i in range(shipPosArray[3]):
        self.boardLayout[shipPosArray[0] - i][shipPosArray[1]] = shipPosArray[4]
          
    if shipPosArray[2] == 2:
      for i in range(shipPosArray[3]):
        self.boardLayout[shipPosArray[0] + i][shipPosArray[1]] = shipPosArray[4]
    
    if shipPosArray[2] == 3:
      for i in range(shipPosArray[3]):
        self.boardLayout[shipPosArray[0]][shipPosArray[1] - i] = shipPosArray[4]
    
    if shipPosArray[2] == 4:
      for i in range(shipPosArray[3]):
        self.boardLayout[shipPosArray[0]][shipPosArray[1] + i] = shipPosArray[4]
  
class ship:
  
  def __init__(self, whichSide, shipType, shipArray):
    self.whichSide = whichSide
    self.shipArray = shipArray
    self.shipType = shipType 
  

playerBoard = board(0, np.full((8,8),0))
botBoard = board(1, np.full((8,8),0))

playerCarrier = ship(0,"carrier", np.array([1,1,1,1,1]))
playerBattleship = ship(0, "battleship", np.array([2,2,2,2]))
playerCruiser = ship(0, "cruiser", np.array([3,3,3]))
playerSubmarine = ship(0, "submarine", np.array([4,4,4]))
playerPatrol = ship(0,"patrol", np.array([5,5]))

botCarrier = ship(1, "carrier", np.array([1,1,1,1,1]))
botBattleship = ship(1, "battleship", np.array([2,2,2,2]))
botCruiser = ship(1, "cruiser", np.array([3,3,3]))
botSubmarine = ship(1, "submarine", np.array([4,4,4]))
botPatrol = ship(1, "patrol", np.array([5,5]))

playerShips = np.array([playerCarrier, playerBattleship, playerCruiser, playerSubmarine, playerPatrol])

botShips = np.array([botCarrier, botBattleship, botCruiser, botSubmarine, botPatrol])

for ship in playerShips:
  playerBoard.placeShip(playerBoard.makeShipPos(ship.shipArray))
  playerBoard.printBoard()

for ship in botShips:
  botBoard.placeShip(botBoard.makeShipPos(ship.shipArray))
  botBoard.printBoard()