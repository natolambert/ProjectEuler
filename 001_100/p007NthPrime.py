'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

from p003 import isprime

i = 3
n = 6
while True:
    if not ( ((n%2)==0) or ((n%5)==0) ):
        if isprime(n):
            i += 1
            if (i>10000): break
    n += 1

print n
