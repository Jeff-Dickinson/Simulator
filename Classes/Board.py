# The Board class handles the construction of the game board, enforcing the rules, stepping through the time steps. 

class Board():
    # Input is the size of the puzzle and user-friendly constraints
    def __init__(self, size_column, size_row):
        self.size_column = size_column
        self.size_row = size_row
        self.board = []
        self.generation = 0

        self.board = [[0] * size_row for i in range(size_column)]
        for i in range(self.size_column):
            for j in range(self.size_row):
                self.board[i][j] = 0
        
        self.buffer = [[0] * size_row for i in range(size_column)]
        for i in range(self.size_column):
            for j in range(self.size_row):
                self.buffer[i][j] = 0
    
    # Main logic loop function. Calls Pre_Update, Update, and Post_Update 
    def Process(self):
        # Does nothing for now
        self.Pre_Update()

        # Check rules for all cells
        self.Update()
        
        # Does nothing for now
        self.Post_Update()

        return self.board

    # Do nothing for now
    def Pre_Update(self):
        print("Pre_Update")
        self.buffer = self.board
    
    # Checks rules for all cells and updates where necessary
    # TODO: Implement a way to only update cells that need it, save unnecessary processing
    def Update(self):
        print("Update")
        cells = [[0] * self.size_row for i in range(self.size_column)]
        # Loop through all the cells... Boundary cells aren't implemented yet
        for row in range(self.size_row):
            for col in range(self.size_column):
                var = self.Get_Live_Neighbor_Count(cell_row = row, cell_col = col)

                # if live and < 2 or > 3, dies
                if self.board[col][row] == 1 and (var < 2 or var > 3):
                    cells[col][row] = 0

                elif self.board[col][row] == 0 and var == 3:
                    cells[col][row] = 1

                # if live and 2 or 3, it lives (default)                
                elif self.board[col][row] == 1 and (var == 2 or var == 3):
                    cells[col][row] = 1
                # if dead and 3, it becomes live
                if var != 0:
                    print("Cell (col,row): ", col, " ", row, " has ", var , " neighbors")
                    
        for row in range(self.size_row):
            for col in range(self.size_column):
                self.board[col][row] = cells[col][row]

    # Do nothing for now
    def Post_Update(self):
        print("Post_Update")
        
    def Heart_Beat(self):
        print("I'm alive!")

    # Print out the board row by row starting at (0,0). Warning: This could take a tremondous amount of RAM and Time
    # TODO: Make this flexible and print chunks
    def Print_Board(self):
        total_board = ""
        concatenated_row = ""
        for row in range(self.size_row):
            for column in range(self.size_column):
                concatenated_row = concatenated_row + str(self.board[column][row]) + " "
            concatenated_row = concatenated_row + "\n"
            total_board = total_board + concatenated_row
            concatenated_row = ""
        print(total_board)

    # Create a glider based around the provided center
    def Create_Glider(self, center_row, center_col):
        #Initial pattern for a glider
        '''
        0 1 0
        0 0 1
        1 1 1 
        '''
        print("Center_row = ", center_row, "\t", "Size_Row = ", self.size_row)
        print("center_col = ", center_col, "\t", "Size_Col = ", self.size_column)
        if self.Within_Bounds(1, center_row, center_col):
            print("Building...")
            self.board[center_col][center_row - 1] = 1
            self.board[center_col][center_row + 1] = 1
            self.board[center_col - 1][center_row + 1] = 1
            self.board[center_col + 1][center_row + 1] = 1
            self.board[center_col + 1][center_row] = 1

    # Given a center and a radius, this function will return true if all of the neighbors are within the boundary of the board
        #
    def Within_Bounds(self, radius, center_row, center_col):

        if((center_row + radius >= 0) and (center_row + radius <= self.size_row) and (center_col + radius >= 0) and (center_col + radius <= self.size_column)):
            return True
        else:
            return False

    # TODO This needs to be revised.
    def Get_Live_Neighbor_Count(self, cell_row, cell_col):
        live_neighbors = 0
        # If it is not a boundary cell, count up its 8 neighbors
        if ( (cell_row in range(1, self.size_row - 1)) and (cell_col in range(1, self.size_column - 1))):
            # Reposition center reference to make looping through the blocks easier
            live_neighbors += self.board[cell_col - 1][cell_row - 1]
            live_neighbors += self.board[cell_col - 1][cell_row]
            live_neighbors += self.board[cell_col - 1][cell_row + 1]
            live_neighbors += self.board[cell_col][cell_row - 1]
            live_neighbors += self.board[cell_col][cell_row + 1]
            live_neighbors += self.board[cell_col + 1][cell_row - 1]
            live_neighbors += self.board[cell_col + 1][cell_row]
            live_neighbors += self.board[cell_col + 1][cell_row + 1]
        
        # Top left corner
        elif (cell_row == 0) and (cell_col == 0):
            live_neighbors += self.board[0][1]
            live_neighbors += self.board[1][1]
            live_neighbors += self.board[1][0]
            live_neighbors += self.board[self.size_column - 1][1]
            live_neighbors += self.board[self.size_column - 1][0]
            live_neighbors += self.board[self.size_column - 1][self.size_row - 1]
            live_neighbors += self.board[0][self.size_row - 1]
            live_neighbors += self.board[1][self.size_row - 1]
            #live_neighbors += 1

        # Bottom left corner
        elif (cell_row == self.size_row - 1) and (cell_col == 0):
            live_neighbors += self.board[1][self.size_row - 1]
            live_neighbors += self.board[0][self.size_row - 2]
            live_neighbors += self.board[1][self.size_row - 2]
            live_neighbors += self.board[0][0]
            live_neighbors += self.board[1][0]
            live_neighbors += self.board[self.size_column - 1][self.size_row - 1]
            live_neighbors += self.board[self.size_column - 1][0]
            live_neighbors += self.board[self.size_column - 2][self.size_row - 2]
            #live_neighbors += 1

        # Top right corner
        elif (cell_row == 0) and (cell_col == self.size_column - 1):
            live_neighbors += self.board[self.size_column - 2][0]
            live_neighbors += self.board[self.size_column - 2][1]
            live_neighbors += self.board[self.size_column - 1][1]
            live_neighbors += self.board[self.size_column - 1][self.size_row - 1]
            live_neighbors += self.board[self.size_column - 2][self.size_row - 1]
            live_neighbors += self.board[0][0]
            live_neighbors += self.board[1][0]
            live_neighbors += self.board[0][self.size_row - 1]
            #live_neighbors += 1

        # Bottom right corner
        elif (cell_row == self.size_row - 1) and (cell_col == self.size_column - 1):
            live_neighbors += self.board[self.size_column - 2][self.size_row - 2]
            live_neighbors += self.board[self.size_column - 2][self.size_row - 1]
            live_neighbors += self.board[self.size_column - 1][self.size_row - 2]
            live_neighbors += self.board[self.size_column - 2][0]
            live_neighbors += self.board[self.size_column - 1][0]
            live_neighbors += self.board[0][0]
            live_neighbors += self.board[0][self.size_row - 1]
            live_neighbors += self.board[0][self.size_row - 2]
            #live_neighbors += 1
        
        # Left Border
        elif (cell_col == 0):
            live_neighbors += self.board[0][cell_row + 1]
            live_neighbors += self.board[0][cell_row - 1]
            live_neighbors += self.board[1][cell_row]
            live_neighbors += self.board[1][cell_row + 1]
            live_neighbors += self.board[1][cell_row - 1]
            live_neighbors += self.board[self.size_column - 1][cell_row]
            live_neighbors += self.board[self.size_column - 1][cell_row + 1]
            live_neighbors += self.board[self.size_column - 1][cell_row - 1]
            #live_neighbors += 1

        # Right Border
        elif (cell_col == self.size_column - 1):
            live_neighbors += self.board[self.size_column - 1][cell_row - 1]
            live_neighbors += self.board[self.size_column - 1][cell_row + 1]
            live_neighbors += self.board[self.size_column - 2][cell_row + 1]
            live_neighbors += self.board[self.size_column - 2][cell_row]
            live_neighbors += self.board[self.size_column - 2][cell_row - 1]
            live_neighbors += self.board[0][cell_row - 1]
            live_neighbors += self.board[0][cell_row]
            live_neighbors += self.board[0][cell_row + 1]
            #live_neighbors += 1

        # Top Border
        elif (cell_row == 0):
            live_neighbors += self.board[cell_col - 1][0]
            live_neighbors += self.board[cell_col - 1][1]
            live_neighbors += self.board[cell_col - 1][self.size_row - 1]
            live_neighbors += self.board[cell_col][self.size_row - 1]
            live_neighbors += self.board[cell_col + 1][self.size_row - 1]
            live_neighbors += self.board[cell_col][1]
            live_neighbors += self.board[cell_col + 1][1]
            live_neighbors += self.board[cell_col + 1][0]
            #live_neighbors += 1

        # Bottom Border
        elif (cell_row == self.size_row - 1):
            live_neighbors += self.board[cell_col - 1][self.size_row - 2]
            live_neighbors += self.board[cell_col - 1][self.size_row - 1]
            live_neighbors += self.board[cell_col - 1][0]
            live_neighbors += self.board[cell_col][self.size_row - 2]
            live_neighbors += self.board[cell_col][0]
            live_neighbors += self.board[cell_col + 1][self.size_row - 2]
            live_neighbors += self.board[cell_col + 1][self.size_row - 1]
            live_neighbors += self.board[cell_col + 1][0]
            #live_neighbors += 1

        # The previous loop would count the cell itself as a neighbor -- Correcting for this
        #live_neighbors -= self.board[cell_col][cell_row]
        return live_neighbors
                    