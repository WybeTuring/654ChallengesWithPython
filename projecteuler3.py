<<<<<<< HEAD
#This function determines if a number is a prime number
def is_prime(x):
    u = 1
    i = 2
    while i < x:
        if x%i == 0:
            u = 0
            break
        else:
            i = i+1
    return u

#This function determines if a number is a prime factor of another
def detprime(x,y):
    if x%y == 0:
        if (is_prime(y)):
            return 1
        else:
            return 0
    else:
        return 0
#This section checks for all the prime factors of a given number, stores them in a list, and returns the largest value
def functionFinal(x):
    import math
    factors = []
    y = x//2
    for i in range(1,y):
        if detprime(x,i) == 1:
            factors.append(i)
    y = len(factors)
    print(factors[y-1])

import time
start_time = time.clock()
print("Enter a number")
num = int(input())
functionFinal(num)
print(time.clock()-start_time)
=======
#This function determines if a number is a prime number
def is_prime(x):
    u = 1
    i = 2
    while i < x:
        if x%i == 0:
            u = 0
            break
        else:
            i = i+1
    return u

#This function determines if a number is a prime factor of another
def detprime(x,y):
    if x%y == 0:
        if (is_prime(y)):
            return 1
        else:
            return 0
    else:
        return 0
#This section checks for all the prime factors of a given number, stores them in a list, and returns the largest value
def functionFinal(x):
    import math
    factors = []
    y = x//2
    for i in range(1,y):
        if detprime(x,i) == 1:
            factors.append(i)
    y = len(factors)
    print(factors[y-1])

import time
start_time = time.clock()
print("Enter a number")
num = int(input())
functionFinal(num)
print(time.clock()-start_time)
>>>>>>> origin/master
