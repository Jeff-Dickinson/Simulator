import sys
import datetime
import os

sys.path.append('Classes')

from Classes import Board, Interface

CURRENT_OS = os.name

# Make a X,Y game board. 0,0 is the upper left corner. 
GameBoard = Board.Board(size_row = 10, size_column = 10)

# Open HWInterface only on the pi
if CURRENT_OS == 'posix':
  HWInterface = Interface.HWInterface(size_row = 10, size_column = 10)

# Seed the board with a pattern
# TODO: Randomize a starting patern or import/create a known pattern
GameBoard.Create_Glider(5,5)
a = datetime.datetime.now()
round_num = 0

while round_num < 15:
  b = datetime.datetime.now()
  if ((b - a).seconds % 2 == 1): # Delay the processing
    game_state = GameBoard.Process()

    # If on posix then we are in the raspberrypi
    if CURRENT_OS == 'posix':
      # Interface
      HWInterface.Process(game_state)  
    else: # Else we are on windows and not connected to the display
      GameBoard.Print_Board()

    round_num += 1
    a = datetime.datetime.now()

if CURRENT_OS == 'posix':
      # Close connection if its open
      HWInterface.CloseConnection()