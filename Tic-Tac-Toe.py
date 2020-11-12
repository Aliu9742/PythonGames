import builtins
from numpy import random
import numpy as np

board = np.full((3,3),5) 
game_round = 0 
who_wins = 5

def display_board():
  print ("    0 1 2")
  print ("0 ", board[0])
  print ("1 ",board[1])
  print ("2 ",board[2])

def player_turn():
  row = builtins.input("choose row from 0 to 2: ")
  row = int(row)
  column = builtins.input("choose column from 0 to 2: ")
  column = int(column)
  if row < 3 and column < 3 and board[row][column] == 5:
    board[row][column] = 0
    display_board()
  else:
    print ("you cannot make a move there")
    player_turn()
#This function places a 0 at the location specified by the user.

def computer_turn():
  check_row = np.sum(board, axis=1)
  check_column = np.sum(board, axis=0)
  check_diagonal = np.diagonal(board)
  check_other_diagonal = np.diagonal(np.fliplr(board))
  if np.sum(check_diagonal) == 7:
    diagonal_pos = 0
    while diagonal_pos < 3:
      if board[diagonal_pos][diagonal_pos] == 5:
        board[diagonal_pos][diagonal_pos] = 1
        display_board()
        return
      diagonal_pos = diagonal_pos + 1
  if np.sum(check_other_diagonal) == 7:
    diagonal_pos = 0
    while diagonal_pos < 3:
      if board [diagonal_pos][-diagonal_pos+2] == 5:
        board[diagonal_pos][-diagonal_pos+2] = 1
        display_board()
        return
      diagonal_pos = diagonal_pos+1
  pos = 0
  while pos < 3:
    if check_column[pos] == 7:
      row_pos = 0
      while row_pos < 3: 
        if board[row_pos][pos] == 5:
          board[row_pos][pos] = 1
          display_board()
          return
        row_pos = row_pos + 1
    if check_row[pos] == 7:
      column_pos = 0
      while column_pos <3:
        if board[pos][column_pos] == 5:
          board[pos][column_pos] = 1
          display_board()
          return
        column_pos = column_pos + 1
    pos = pos + 1
     
  if np.sum(check_diagonal) == 5:
    diagonal_pos = 0
    while diagonal_pos < 3: 
      if board[diagonal_pos][diagonal_pos] == 5:
        board[diagonal_pos][diagonal_pos] = 1
        display_board()
        return
      diagonal_pos = diagonal_pos + 1
  if np.sum(check_other_diagonal) == 5:
    diagonal_pos = 0
    while diagonal_pos <3:
      if board [diagonal_pos][-diagonal_pos+2] ==5:
        board[diagonal_pos][-diagonal_pos+2] = 1
        display_board()
        return
      diagonal_pos = diagonal_pos + 1
  pos = 0 
  while pos < 3:
    if check_column[pos] == 5:
      row_pos = 0
      while row_pos < 3:
        if board[row_pos][pos] ==5:
          board[row_pos][pos] = 1
          display_board()
          return
        row_pos = row_pos + 1
    if check_row[pos] == 5:
      column_pos = 0
      while column_pos <3:
        if board[pos][column_pos] ==5:  
          board[pos][column_pos] = 1
          display_board()
          return
        column_pos = column_pos + 1
    pos = pos +1
  
  row_computer = random.randint(3) 
  column_computer = random.randint(3)
  while board[row_computer][column_computer] != 5:
    row_computer = random.randint(3) 
    column_computer = random.randint(3)
  board[row_computer][column_computer] = 1
  display_board()
  print("the computer made a move at", row_computer,column_computer)



def win_condition (turn_number):
  check_column = np.sum(board, axis = 0)
  #print("column is", check_column)
  check_row = np.sum(board, axis = 1)
  #print("row is", check_row)
  check_diagonal = np.diagonal(board)
  #print("diagonal is", check_diagonal)
  check_other_diagonal = np.diagonal(np.fliplr(board))
  #print("other diagnal is", check_other_diagonal)
  if (turn_number % 2) ==0:
    if np.sum(check_diagonal) == 0 or np.sum(check_other_diagonal) ==0:
      print("player win")
      who_wins = 0
      return who_wins
    i = 0
    while i < 4:
      if i < 3: 
        if check_column[i] == 0 or check_row[i] ==0:
          print("player win")
          who_wins = 0
          return who_wins
      i = i+1
      if i ==4:
        who_wins = 5
        return who_wins
  if (turn_number % 2) !=0:
    if np.sum(check_diagonal) == 3 or np.sum(check_other_diagonal) ==3:
      print("computer win")
      who_wins = 1
      return who_wins
    i = 0
    while i < 4:
      if i < 3: 
        if check_column[i] == 3 or check_row[i] == 3:
          print("computer win")
          who_wins = 1
          return who_wins
      i = i+1
      if i ==4:
        who_wins = 5
        return who_wins
  
def game_turn(turn_number):
  if (turn_number % 2) == 0:
    player_turn()
  elif turn_number < 10:
    computer_turn() 
#this function controls the flow of the game.

print("Hi there! Welcome to a game of tic-tac-toe.")
display_board()
while game_round < 10:
  print("It is round", game_round)
  game_turn(game_round)
  win_condition(game_round)
  who_wins = win_condition(game_round)
  print("-----------")
  if who_wins == 5:
    game_round += 1
  else: 
    break