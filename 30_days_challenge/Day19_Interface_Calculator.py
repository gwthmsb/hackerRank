class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


"""
Could be implemented better
"""
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor_sum = n
        for i in xrange(1, n / 4 + 1):
            if n % i == 0:
                divisor_sum += i
        if n % 3 == 0:
            divisor_sum += n / 3
        if n % 2 == 0:
            divisor_sum += n / 2

        return divisor_sum


n = int(raw_input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)