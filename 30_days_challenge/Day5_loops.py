"""
For given number n, print "n x i = n*i" where i is in range 1-10

"""

if __name__ == '__main__':
    n = int(raw_input())

    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n*i))
