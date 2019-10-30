"""
Given a array A, print array elements in reverse order separated by space

"""

from __future__ import print_function


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    print(*arr)

