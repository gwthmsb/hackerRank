#!/bin/python
from __future__ import print_function
import sys


def bubble_sort(n, a):
    no_of_swaps = 0
    for i in xrange(n):
        for j in xrange(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                no_of_swaps +=1
    return no_of_swaps

def print_output(a, n, no_of_swaps):
    print("Array is sorted in {} swaps.".format(no_of_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n-1]))


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
no_of_swaps = bubble_sort(n, a)
# Write Your Code Here
print_output(a, n, no_of_swaps)

