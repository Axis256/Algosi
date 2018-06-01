import math
#from scipy.special import comb
import timeit

a, b, n = map(int, input().split())

def check_wonderful(value, a, b):
    while value > 0:
        if value % 10 == a or value % 10 == b:
            value //= 10
        else:
            return False
    return True

def binomial_coefficient(a, b):
    if a == 0 or b == 0:
        return 1
    elif a == 1 or b == 1:         # see georg's comment
        return a + b
    else:                # will be executed only if y != 1 and y != x and x <= y
        x = math.factorial(a)
        y = math.factorial(b)
        n = math.factorial(a + b)  # that appears to be useful to get the correct result
        return (n // (x * y))

count = 0

begin = timeit.default_timer()

for i in range(n + 1):
    if check_wonderful(a * i + b * (n - i), a, b):
        count += binomial_coefficient(i, n - i)

end = timeit.default_timer()

print(count % 1000000007)
#