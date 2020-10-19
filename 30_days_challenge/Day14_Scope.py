"""
Objective
Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

The absolute difference between two integers,  and , is written as . The maximum absolute difference between two
integers in a set of positive integers, , is the largest absolute difference between any two integers in .

The Difference class is started for you in the editor. It has a private integer array () for storing  non-negative
integers, and a public integer () for storing the maximum absolute difference.

Task
Complete the Difference class by writing the following:

* A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
* A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the
maximum_difference instance variable.
Input Format

You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in  lines of
input; the first line contains , and the second line describes the  array.

Constraints
1<=N<=10
1<=elements[i]<=100 where 0<=i<=N-1

, where
Output Format

You are not responsible for printing any output; the Solution class will print the value of the  instance variable.

Sample Input

3
1 2 5
Sample Output

4


"""


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in xrange(len(self.__elements)):
            for j in xrange(i, len(self.__elements)):
                absolute_diff = abs(self.__elements[i] - self.__elements[j])
                if abs(absolute_diff) > self.maximumDifference:
                    self.maximumDifference = absolute_diff


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference