import math

# The Node class is in here because these functions require the node class and so do the other classes.
# I would remake this so that the Map class hold all of these functions, but that would take more time than I have.
# If I were to leave this class in the classes.py file, I would get an error because the classes.py file would
# import nodeFunctions.py, and nodeFunctions.py would import classes.py


class Node:
    """
    This class makes a node with the parent node and the position this node would be in.
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # The distance from the starting node to this node
        self.h = 0  # The distance from this node to the end
        self.f = 0  # g and h added together

    def __str__(self):  # Prints the coordinates of the node
        string_to_print = "Coordinates: {0}".format(self.position)
        return string_to_print


def current_node_and_index(open_list):
    """
    Returns a tuple that has the current workable node and its index in the open list

    :param open_list: The list containing all available nodes

    :return: A tuple with (current_node, index)
    """

    # By default, choose the first node.
    current_node = open_list[0]
    index_of_current = 0

    for i in range(0, len(open_list)):
        if open_list[i].f < current_node.f:  # Judge based on f because the lower the f, the better. A lower
            current_node = open_list[i]      # f means that taking that node would lead to a more optimal path
            index_of_current = i
    return current_node, index_of_current


def get_neighbors(current_node, maze):
    """
    Gets the neighbors of the current node

    :param current_node: The current node
    :param maze: The whole map

    :return: A list with the available neighbors of the current node.
    """

    neighbors = []
    potential_neighbors = [  # The positions of the potential neighbors
        (-1, 0),  # One above
        (0, -1),  # One left
        (1, 0),   # One below
        (0, 1),    # One right
        # (1, 1),
        # (-1, 1), # These will make it so that diagonal nodes can be neighbors
        # (1, -1),
        # (-1, -1)
    ]

    for position in potential_neighbors:
        pos_of_node = (current_node.position[0] + position[0], current_node.position[1] + position[1])
        len_of_maze_y = len(maze) - 1  # Subtract from the length to be able to compare with pos_of_node
        len_of_maze_x = len(maze[0]) - 1  # Choose first list because all lists have the same length

        if ((pos_of_node[0] > len_of_maze_y) or (pos_of_node[0] < 0) or      # If pos is not within the range of the
                (pos_of_node[1] > len_of_maze_x) or (pos_of_node[1] < 0) or  # first nested list or second nested list
                (maze[pos_of_node[0]][pos_of_node[1]] != 0)):                # or if the value at that point is not 0
            continue                                                         # skip that neighbor and move to the next.

        created_node = Node(current_node, pos_of_node)
        neighbors.append(created_node)  # Add the node to the neighbors list

    return neighbors


def acceptable_neighbors(neighbors, closed_list, open_list, current_node, end_node):
    """
    Returns a list of neighbors that aren't already in the closed list or open list

    :param neighbors: The neighbors found by the "get_neighbors" function
    :param closed_list: The list with all the nodes that have been run through already
    :param open_list: The list with the nodes that are being worked on
    :param current_node: The current node
    :param end_node: The final node

    :return: A list a nodes
    """

    useful_neighbors = []

    for neighbor in neighbors:  # Run through each neighbor
        is_in_closed = False
        is_in_open = False

        for closed_node in closed_list:
            if neighbor.position == closed_node.position:  # If the position of the neighbor matches one in the closed
                is_in_closed = True                        # list, set is_in closed to True
                break                                      # break so that it can immediately continue if True

        if is_in_closed:                                   # If it was found in the closed list, skip it.
            continue

        neighbor.g = current_node.g + 1  # Add one because this node is now one block away from the current node.
        neighbor.h = math.sqrt(abs(neighbor.position[0] - end_node.position[0]) +  # Find dist from this node to the
                               abs(neighbor.position[1] - end_node.position[1]))   # end node. I used Distance Formula
        neighbor.f = neighbor.g + neighbor.h

        for open_node in open_list:
            if (neighbor.position == open_node.position) and (neighbor.g >= open_node.g):
                is_in_open = True  # If the node matches the position with on in the open list AND the g is greater
                break              # we don't want it. Why? For a cleaner and more efficient path.

        if is_in_open:
            continue

        useful_neighbors.append(neighbor)

    return useful_neighbors


def a_star(the_map):
    """
    Returns the path from start to finish

    the_map: A Map object to use

    :return: The path from start to finish. If no path is possible, return None
    """

    maze = the_map.map
    start = the_map.startPoint
    end = the_map.endPoint
    starting_node = Node(None, start)
    ending_node = Node(None, end)
    open_list = [starting_node]
    closed_list = []

    while len(open_list) != 0:
        # print(open_list)
        current_node, index_of_current = current_node_and_index(open_list)

        open_list.pop(index_of_current)   # Remove from open list because it is chosen
        closed_list.append(current_node)  # Move to the closed list because it is chosen

        if current_node.position == ending_node.position:
            start_to_finish = []  # List of coordinates from start to finish
            while current_node is not None:                     # current_node will be set to its parent. The beginning
                start_to_finish.append(current_node.position)   # node has a parent of None, so the loop will break
                current_node = current_node.parent
            start_to_finish.reverse()
            return start_to_finish  # Return the list of coordinates

        neighbors = get_neighbors(current_node, maze)
        useful_neighbors = acceptable_neighbors(neighbors, closed_list, open_list, current_node, ending_node)

        for node in useful_neighbors:
            open_list.append(node)

    return None

