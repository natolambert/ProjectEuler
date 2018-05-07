'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

n = 600851475143

def isprime(n):
    if (n < 2):
        raise ValueError, 'can only check primes greater than 1'
    # Basic isprime function
    i = 2
    while i <= sqrt(n):
        if (n % i) == 0:
            return False
        i += 1
    return True

# # print '1 ', isprime(1)
# print '3 ', isprime(3)
# print '4 ', isprime(4)
# print '5 ', isprime(5)
# print '6 ', isprime(6)

def LargestPrime(n):
    i = 2
    maxPrime = 0
    '''
    Iterate all through all prime numbers to find largest prime.
    - For each prime, divide by the prime repeating until a prime is no longer divisible
    - Iterate through each of the primes
    - When i is greater than n, check and n should be prime which is your prime factor
    '''
    while True:
        # Iterate through primes
        if isprime(i):
            if (n % i) == 0:
                n /= i
            else: i+=1

            if (i-1 >= n): return i
        else: i+=1

# print 'LargestPrime of 21 ', LargestPrime(600851475143)
