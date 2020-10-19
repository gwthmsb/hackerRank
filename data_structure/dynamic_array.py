#!/bin/python3

"""
Hackerank problem: https://www.hackerrank.com/challenges/dynamic-array/problem

"""


import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


last_answer = 0
seq_len = 0
dynamic_seq_lists = list()


def define_dyn_seq_list(list_len):
    global dynamic_seq_lists, seq_len
    seq_len = list_len
    for i in range(list_len):
        dynamic_seq_lists.append(list())


def query_type1(x, y):
    global dynamic_seq_lists, seq_len, last_answer
    seq_index = (x ^ last_answer) % seq_len
    seq = dynamic_seq_lists[seq_index]
    seq.append(y)
    dynamic_seq_lists[seq_index] = seq


def query_type2(x, y):
    global dynamic_seq_lists, seq_len, last_answer
    seq_index = (x ^ last_answer) % seq_len
    seq = dynamic_seq_lists[seq_index]
    sl = len(seq)
    last_answer = seq[y % sl]
    return last_answer


def dynamicArray(n, queries):
    define_dyn_seq_list(n)
    results = list()
    for query in queries:
        if query[0] == 1:
            query_type1(query[1], query[2])
        elif query[0] == 2:
            results.append(query_type2(query[1], query[2]))
    # Write your code here
    return results

if __name__ == '__main__':
    n = 2
    queries = [ (1, 0, 5),
                (1, 1, 7),
                (1, 0, 3),
                (2, 1, 0),
                (2, 1, 1)]

    result = dynamicArray(n, queries)

    print(result)

