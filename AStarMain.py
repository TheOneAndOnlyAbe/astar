######################################################################
# Author: Abraham Moreno
# Username: morenoa2
#
# AStar Path Finding Project
#
# Purpose: Find the shortest path from start to finish while avoiding obstacles
######################################################################
# Acknowledgements:
# 1. Used https://en.wikipedia.org/wiki/A*_search_algorithm for the pseudo code and to see how it works
# 2. Since I'm comfortable with Javascript, using https://www.youtube.com/watch?v=S4yQYiAECnM to get an idea of how
#    the drawing process would work. I can't use P5 because it's for Javascript.
# 3. Used test suite code by Scott Heggen
# 4. https://stackoverflow.com/questions/4383571/importing-files-from-different-folder to figure out how to import
#    from other folders
# 5. https://www.youtube.com/watch?v=YXPyB4XeYLA FreeCodeCamp 5 hour tutorial on Tkinter and made a file in here
#    to show my journey learning Tkinter
# 6. https://stackoverflow.com/questions/5543815/how-to-change-button-color-with-tkinter Showed me how to edit the
#    configuration of Tkinter objects.
# 7. https://stackoverflow.com/questions/42807745/how-to-create-a-grid-of-buttons-in-tk-with-functions-that-are-called-
#    using-their/42809770 showed how lambda can be useful to pass in variables for the "command" configuration
# 8. https://stackoverflow.com/questions/37731654/how-to-retrieve-the-row-and-column-information-of-a-button-and-use-
#    this-to-alter showed how to get th column and row info from a button
# 9. https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270 Showed me how to make a Tkinter
#    button redirect to a web link.
#
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
# How AStar Path Finding works:
# AStar Path Finding attempts to find the shortest path from the starting point to the ending point while keeping
# barriers in mind. It does this by doing the calculation g + h = f. G is the distance from the starting position to the
# current position. H is the distance from the current position to the end position. F is the addition of G and H. AStar
# will try to choose the node with the lowest F value until it reaches the end.

from helperFiles.classes import MainScreen
from tkinter import *


def main():
    """
    Main function of the program
    """

    root = Tk()  # Main thing used to run Tkinter

    screen = MainScreen(root)  # Run the whole program
    screen.gen_map()  # Generate map and buttons
    screen.gen_buttons()

    root.mainloop()  # A loop that keeps the program open until the user exits


if __name__ == '__main__':
    main()
