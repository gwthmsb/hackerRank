"""
Slice the given string by even and odd index

"""

n = int(raw_input())
for i in range(0,n):
    string = raw_input()
    print(string[0::2]+" "+string[1::2])
