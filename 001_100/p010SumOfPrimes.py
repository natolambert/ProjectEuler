'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from p003PrimeFactor import isprime

summ = 0
for i in range(2,2000000):
    if isprime(i):
        summ += i

print(summ)
