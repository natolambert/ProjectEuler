'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

from itertools import combinations

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome():
    # Returns largest palindrome of 3dig times 3dig numbers
    nums = range(999,99,-1)
    max_pali = 0
    for (n1,n2) in combinations(nums,2):
        prod = n1*n2
        if is_palindrome(prod):
            if (prod > max_pali):
                max_pali = prod
    return max_pali

print largest_palindrome()
