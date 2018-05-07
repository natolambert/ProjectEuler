'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def pythag_pairs(c):
    # takes in an int and returns a list of pythagorean pairs
    # ie given c, return [a,b] so that a^2 + b^2 = c^2
    l = []

    # Too short
    if (c < 2):
        return l

    # a < b < c gives us a^2 < c^2/2 < b^2 < c^2
    endr = int(math.ceil(c / math.sqrt(2)))
    for a in range(3,endr):
        b = math.sqrt(c**2-a**2)
        if (b== int(b)):
            l.append([a,int(b)])
    return l

print(pythag_pairs(5))

# intialize c
c = 3
loop = True
while (loop == True):
    l = pythag_pairs(c)

    for ab in l:

        a = ab[0]
        b = ab[1]
        print(ab)
        print(int(a**2 + b**2))
        print(int(c**2))
        if (a+b+c == 1000):
            print('Answer is the Following:')
            print('...a: ', a)
            print('...b: ', b)
            print('...c: ', c)
            a_ans = a
            b_ans = b
            c_ans = c
            loop = False
            break

    c+= 1

print('product is: ', a_ans*b_ans*c_ans)
