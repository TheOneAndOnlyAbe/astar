import copy
from tkinter import *
from helperFiles.nodeFunctions import a_star
import webbrowser


class Map:
    """
    This class will make the map for the program
    """

    def __init__(self):
        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.startPoint = None  # Start, End, and Obstacles will be given in tuples
        self.endPoint = None


class MainScreen:
    """
    This class is the screen. It makes all of the buttons and interacts with the background scripts.
    """

    def __init__(self, root):
        self.map = Map()
        self.rows = len(self.map.map)  # Find the amount of rows and cols in the map
        self.columns = len(self.map.map[0])
        self.root = root
        self.button_images = self.gen_button_images()
        self.buttons = []
        self.function_buttons = []
        self.start_button = self.end_button = self.color = None
        self.start_made = self.end_made = False

    def gen_map(self):
        """
        Generates the map and makes a matrix representation of it to match the binary map from Map()
        """

        for i in range(self.rows):
            self.buttons.append([])
            for k in range(self.columns):
                my_button = Button(self.root, padx=20, pady=10, bg="white",
                                   command=lambda row=i, column=k: self.set(row, column))  # Make a button matrix
                my_button.grid(row=i, column=k)
                # print(my_button)
                self.buttons[i].append(my_button)  # This replicates the map matrix thanks to line 44
        # print(self.buttons)

    def gen_button_images(self):
        """
        Makes the images for the buttons usable
        :return: A list of button images
        """
        images_names = ["start_button", "end_button", "reset_start", "reset_end",
                        "add_barrier", "remove_barrier", "reset_map", "find_path", "my_portfolio"]
        button_images = []

        for i in images_names:
            link = "image/buttonImages/" + i + ".png"
            button_images.append(PhotoImage(file=link))  # Push all image objects into the button_images list

        return button_images

    def gen_buttons(self):
        """
        Generates the buttons that provide the function
        """

        self.gen_button_images()
        c = self.columns

        # Order of the buttons in self.function_buttons:
        # start_button, end_button, reset_start, reset_end, add_barrier, remove_barrier, reset_map, find_path
        for i in range(9):
            self.function_buttons.append(Button(self.root, image=self.button_images[i], border=0))
        # print(self.function_buttons)
        for i in range(0, 4, 2):
            self.function_buttons[i].grid(row=i, column=c+10, padx=20)
            self.function_buttons[i+4].grid(row=i+4, column=c+10, padx=20)  # These signify the position of the buttons
            self.function_buttons[i+1].grid(row=i, column=c+11, padx=20)
            self.function_buttons[i+5].grid(row=i+4, column=c+11, padx=20)

        self.start_button = self.function_buttons[0]  # Since the start and end buttons are VERY important, they
        self.end_button = self.function_buttons[1]    # hold their own variables in the class

        self.start_button.configure(command=lambda: self.set_color("#00ab09"))
        self.end_button.configure(command=lambda: self.set_color("#b80000"))
        self.function_buttons[2].configure(command=self.new_start_point, state=DISABLED)
        self.function_buttons[3].configure(command=self.new_end_point, state=DISABLED)
        self.function_buttons[4].configure(command=lambda: self.set_color("black"))  # Since I can't iterate through
        self.function_buttons[5].configure(command=lambda: self.set_color("white"))  # these, I just configured what
        self.function_buttons[6].configure(command=self.reset_map)                   # was different
        self.function_buttons[7].configure(command=self.find_path, state=DISABLED)

        # My Portfolio button is separate because it's just a small extra feature. It doesn't do anything to the
        # program.
        link = "https://abesportfolio.herokuapp.com/"
        self.function_buttons[8].configure(command=lambda: webbrowser.open(link, new=1))
        self.function_buttons[8].grid(row=8, column=c+10, padx=20)

    def set(self, row, column):
        """
        Decides what the current color will do

        :param row: The row the node is at
        :param column: The column the node is at
        """

        if self.color == "#00ab09":  # Green signifies the starting position
            # print("color is green")
            self.buttons[row][column].configure(background=self.color, state=DISABLED)
            self.start_button.configure(state=DISABLED)  # Disable button so user doesn't keep clicking
            self.function_buttons[2].configure(state=ACTIVE)  # Set the reset button to active
            self.color = None  # Set color to none so that the matrix is not affected if it is clicked.
            self.start_made = True
            self.check_start_end()

            self.map.startPoint = (row, column)
            # print(self.map.startPoint)
        elif self.color == "#b80000":
            # print("color is red")
            self.buttons[row][column].configure(background=self.color, state=DISABLED)
            self.end_button.configure(state=DISABLED)
            self.function_buttons[3].configure(state=ACTIVE)
            self.color = None
            self.end_made = True
            self.check_start_end()

            self.map.endPoint = (row, column)
            # print(self.map.endPoint)
        elif self.color == "black":
            self.buttons[row][column].configure(background=self.color)  # Doesn't have as many limitations as the others
            self.map.map[row][column] = 1                            # because it doesn't really matter.
        elif self.color == "white":
            self.buttons[row][column].configure(background=self.color)
            self.map.map[row][column] = 0

    def set_color(self, color):
        """
        Controls the color that the clickable matrix will be set to.

        :param color: The color that depends on which button was pressed.
        """

        self.color = color
        # print(self.color)

    def new_start_point(self):
        """
        Resets the the node which was the starting point
        """

        i = self.map.startPoint[0]  # Since the visual matrix represents the matrix in Map(), we can use the same
        k = self.map.startPoint[1]  # starting and ending point
        self.map.map[i][k] = 0
        self.buttons[i][k].configure(state=NORMAL, bg="white")
        self.start_button.configure(state=ACTIVE)
        self.function_buttons[2].configure(state=DISABLED)
        self.start_made = False
        self.color = None
        self.check_start_end()  # calling this method will make the "Find Path" button inactive
        # self.map.startPoint = None

    def new_end_point(self):
        """
        Resets the node which was the end point
        """

        i = self.map.endPoint[0]
        k = self.map.endPoint[1]
        self.map.map[i][k] = 0
        self.buttons[i][k].configure(state=NORMAL, bg="white")
        self.end_button.configure(state=ACTIVE)
        self.function_buttons[3].configure(state=DISABLED)
        self.end_made = False
        self.color = None
        self.check_start_end()

    def reset_map(self):
        """
        Resets the map and resets the Map()
        """

        self.color = self.map.startPoint = self.map.endPoint = None
        for i in range(self.rows):
            for k in range(self.columns):  # Make all buttons in the matrix the way it was
                self.map.map[i][k] = 0
                self.buttons[i][k].configure(bg="white", state=NORMAL)
        self.function_buttons.clear()
        self.gen_buttons()
        self.start_made = self.end_made = False
        self.check_start_end()

    def find_path(self):
        """
        Finds the path from the starting to the finishing node
        """

        self.color = "white"
        for button in self.function_buttons:
            button.configure(state=DISABLED)  # Disables all buttons so that the user can't edit the final map.
        self.function_buttons[6].configure(state=ACTIVE)  # Activates reset button
        self.function_buttons[8].configure(state=ACTIVE)
        for i in range(self.rows):
            for k in range(self.columns):
                self.buttons[i][k].configure(state=DISABLED)  # This is so that the user cant edit the final map
        path = a_star(self.map)
        if path is not None:
            path = path[1:-1]  # Removes the starting point and the ending point
            for position in path:  # Get the path from start to finish and display it using a yellow color
                self.buttons[position[0]][position[1]].configure(bg="#09578f", state=DISABLED)
        else:
            for i in self.buttons:
                for button in i:  # If a path is not possible, all buttons in matrix will turn red
                    button.configure(bg="#b80000", state=DISABLED)

    def check_start_end(self):
        """
        Basically an and gate. This function will make it so that the "Find Path" button activates only when the
        starting node and the ending node are chosen.
        """

        if self.end_made and self.start_made:
            self.function_buttons[7].configure(state=ACTIVE)
        else:
            self.function_buttons[7].configure(state=DISABLED)
