import math
import numba as nb

@nb.njit(cache = True)
def is_prime(n):
    if n%2 == 0 and n>2:
        return 0
    for i in range(3, int(math.sqrt(n))+1,2):
        if n%i ==0:
            return 0
    return 1

@nb.njit(cache = True)
def detprime(x,y):
    if x%y == 0:
        if(is_prime(y)):
            return 1
        else:
            return 0
    else:
        return 0

@nb.njit(parallel = True)
def functionFinal(x):
    factors = [1]
    y = x//2
    for i in nb.prange(1,y): #check in parallel
        if detprime(x,i) == 1:
            factors[-1] = i
    return factors[-1]

print("Enter a number")
num = input()
print(functionFinal(num))
