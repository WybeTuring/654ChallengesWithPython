def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x*factorial(x-1))
def sumint(n):
    sum = 0
    th = str(n)
    for i in range(0,len(th)):
        sum += int(th[i])
    return sum
print(sumint(factorial(100)))