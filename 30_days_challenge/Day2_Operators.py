"""
Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are  lines of numeric input:
The first line has a double,  (the cost of the meal before tax and tip).
The second line has an integer,  (the percentage of  being added as tip).
The third line has an integer,  (the percentage of  being added as tax).

Output Format

Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).

Sample Input

12.00
20
8
Sample Output

15

"""

from __future__ import division
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = float(meal_cost * tip_percent / 100) # division should be from __future__ module
    tax_cost = float(meal_cost * tax_percent / 100)
    total_cost = meal_cost + tip_cost + tax_cost
    return math.trunc(total_cost+0.5)

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    print(solve(meal_cost, tip_percent, tax_percent))


def test_solve():
    assert 115 == solve(100, 8, 7)
    assert 141 == solve(111, 13, 14)
