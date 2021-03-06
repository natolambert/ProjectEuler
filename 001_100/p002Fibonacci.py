'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

n = 4000000
x1 = 1
x2 = 1
x = 0
sumf = 0

while (x < n):
    x = x1+x2
    if not (x % 2): sumf += x
    x2 = x1
    x1 = x

print sumf
#
# def fib(n, value=0):
#     if n < 2:
#         return 1
#     return fib(n-2)+fib(n-1)
