'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''

n = range(1,101)

sum_sqrd = sum(x**2 for x in n)
sqrd_sum = sum(n)**2

diff = sqrd_sum - sum_sqrd
print diff
