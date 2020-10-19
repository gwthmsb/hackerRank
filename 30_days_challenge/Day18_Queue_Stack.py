import sys
import Queue


class Solution:
    # Write your code here
    def __init__(self):
        self.queue = Queue.Queue(1000)
        self.stack = Queue.LifoQueue(1000)

    def pushCharacter(self, c):
        self.stack.put(c)

    def enqueueCharacter(self, c):
        self.queue.put(c)

    def dequeueCharacter(self):
        return self.queue.get()

    def popCharacter(self):
        return self.stack.get()


# read the string s
s = raw_input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l / 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write("The word, " + s + ", is a palindrome.")
else:
    sys.stdout.write("The word, " + s + ", is not a palindrome.")

