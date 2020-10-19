
"""

Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a  2D Array, A :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

"""
from __future__ import print_function
from data_structure import OrderedDict

def __main__():
    """

    row_size = raw_input(prompt="Enter row size")
    column_size = raw_input(prompt="Enter column size")
    subset_array_size = raw_input(prompt="Enter subset array size")

    """
    row_size, column_size, subset_array_size = 6, 6, 3
    twoD_array=[[],[]]

    for _ in xrange(6):
        twoD_array.append(map(int, raw_input().rstrip().split()))

    subset_sum_dict = add_possible_subset(row_size, column_size, subset_array_size)
    calculate_subset_sum(twoD_array, subset_sum_dict, 3)
    max_i = max(subset_sum_dict, key=subset_sum_dict.get)

    print_sub_set(max_i, twoD_array)

    max_sum = max(subset_sum_dict.values())
    print(max_sum)


def add_possible_subset(row_size=6, column_size=6, subset_array_size=3):
    subset_sum_dict = OrderedDict()
    for i in xrange(0, row_size-subset_array_size+1):
        for j in xrange(0, column_size-subset_array_size+1):
            subset_sum_dict["{},{}".format(i, j)] = 0
    return subset_sum_dict



def calculate_subset_sum(twoD_array, subset_sum_dict, subset_array_size=3):
    for key in subset_sum_dict.keys():
        row, col = map(int, key.split(",", 1))
        sum = 0
        for i in xrange(row, row+subset_array_size, 2):
            for j in xrange(col, col+subset_array_size):
                sum += twoD_array[i][j]
        mid_i, mid_j = row + int(subset_array_size/2), col + int(subset_array_size/2)
        sum += twoD_array[mid_i][mid_j]
        subset_sum_dict["{},{}".format(row, col)] = sum


def print_sub_set(max_i, twoD_array):
    row, col = map(int, max_i.split(",", 1))
    for i in xrange(row, row + 3, 2):
        for j in xrange(col, col + 3):
            print(twoD_array[i][j], end=" ")
        print()
        if i == row + 3 - 1:
            break
        print(" {}".format(twoD_array[row + 1][col + 1]))


def test_add_possible_subset():
    d = add_possible_subset()
    assert 16 == len(d)


def test_calculate_subset_sum():
    subset_sum_dict = add_possible_subset()
    twoD_array = [[1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0],
                  [0, 0, 2, 4, 4, 0],
                  [0, 0, 0, 2, 0, 0],
                  [0, 0, 1, 2, 4, 0]]
    calculate_subset_sum(twoD_array, subset_sum_dict, 3)

    print(subset_sum_dict)
    max_i = max(subset_sum_dict, key=subset_sum_dict.get)

    print_sub_set(max_i, twoD_array)