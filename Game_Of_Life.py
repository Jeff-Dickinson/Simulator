import sys
import datetime

sys.path.append('Classes')

from Classes import Board

# Make a X,Y game board. 0,0 is the upper left corner. 
GameBoard = Board.Board(size_row = 10, size_column = 10)

# Seed the board with a pattern
# TODO: Randomize a starting patern or import/create a known pattern
GameBoard.Create_Glider(5,5)
a = datetime.datetime.now()
var = 0

while var < 5:
  b = datetime.datetime.now()
  if ((b - a).seconds % 2 == 1):
    GameBoard.Update()
    GameBoard.Print_Board()
    var += 1
    a = datetime.datetime.now()
'''
GameBoard.Get_Live_Neighbor_Count(5,5)
GameBoard.Print_Board()

GameBoard.Update()
GameBoard.Print_Board()

GameBoard.Update()
GameBoard.Print_Board()

GameBoard.Update()
GameBoard.Print_Board()

GameBoard.Update()
GameBoard.Print_Board()

GameBoard.Update()
GameBoard.Print_Board()

GameBoard.Update()
GameBoard.Print_Board()
'''