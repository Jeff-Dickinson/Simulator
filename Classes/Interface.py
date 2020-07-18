# This class handles the interface with the Nextion HMI Display

import time
import serial

g_terminate_string = bytes([255]) + bytes([255]) + bytes([255])
g_clear_screen = 'cls WHITE'.encode("utf-8") + g_terminate_string
g_black_pic_id = '0'

class HWInterface():
    # Connect to the display and clear the screen 
    def __init__(self, size_column, size_row):
        self.size_row = size_row
        self.size_column = size_column
        self.connection = serial.Serial("/dev/ttyAMA0") # Open the port
        self.connection.baudrate = 38400 # Note, this isn't the default baudrate but one I've set it to
        print('Port opened.')
        self.connection.write(g_clear_screen) # Clear the screen

    def CloseConnection(self):
        self.connection.close()

    # Main logic loop function. Calls Pre_Update, Update, and Post_Update 
    def Process(self, board_state):
        # Clear the screen
        self.Pre_Update()

        # Write new dots
        self.Update(board_state)
        
        # Does nothing for now
        self.Post_Update()

    # Do nothing for now
    def Pre_Update(self):
        self.connection.write(g_clear_screen) # clear the screen
    
    # Send commands to update based off the game state
    def Update(self, board_state):
        command_str = 'pic '
        for row in range(self.size_row):
            for column in range(self.size_column):
                if board_state[column][row] == 1:
                    # If the board state is 1, that means to print it
                    temp_str = command_str + str(row) + ',' + str(column) + ',0'
                    self.connection.write(temp_str.encode("utf-8") + g_terminate_string)

                

    # Do nothing for now
    def Post_Update(self):
        print("Post_Update")
        
    def Heart_Beat(self):
        print("I'm alive!")


                    
