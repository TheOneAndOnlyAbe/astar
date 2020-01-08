from helperFiles.nodeFunctions import *
from helperFiles.classes import *
import sys


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def a08_test_suite():

    #################################################################
    #                      SETUP FOR TESTS                          #
    #################################################################

    my_map = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Small sample of nodes and open list
    node1 = Node((0, 0), (6, 1))
    node1.f = node1.g = node1.h = 0
    node2 = Node((3, 4), (0, 0))
    node2.f = node2.g = node2.h = 2
    node3 = Node((6, 2), (9, 5))
    node3.f = node3.g = node3.h = 4
    node4 = Node((0, 1), (2, 0))
    node4.f = node4.g = node4.h = 9

    closedNode1 = Node(None, (5, 1))
    closedNode2 = Node(None, (1, 0))
    closedNode3 = Node(None, (3, 0))

    # Switch up the order of the nodes in the list
    open_list = [node1, node2, node3, node4]
    open_list2 = [node3, node4, node1, node2]
    open_list3 = [node1, node4, node2, node3]
    open_list4 = [node4, node1, node2, node3]

    neighbors = get_neighbors(node1, my_map)
    neighbors2 = get_neighbors(node2, my_map)
    neighbors3 = get_neighbors(node3, my_map)
    neighbors4 = get_neighbors(node4, my_map)

    closed_list = []
    closed_list2 = [closedNode1, closedNode2, closedNode3]
    for i in neighbors3:
        closed_list.append(i)

    #################################################################
    #                TESTING BEGINS BELOW HERE                      #
    #################################################################

    testit(current_node_and_index(open_list) == (node1, 0))
    testit(current_node_and_index(open_list2) == (node1, 2))
    testit(current_node_and_index(open_list3) == (node1, 0))
    testit(current_node_and_index(open_list4) == (node1, 1))

    testit(len(neighbors) == 3)
    testit(len(neighbors2) == 2)
    testit(len(neighbors3) == 3)
    testit(len(neighbors4) == 3)

    testit(len(acceptable_neighbors(neighbors, closed_list, [], node1, node4)) == 3)
    testit(len(acceptable_neighbors(neighbors4, closed_list2, [], node4, node2)) == 1)


if __name__ == "__main__":
    a08_test_suite()
