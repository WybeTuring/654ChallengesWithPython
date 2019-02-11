def countDivisors(n):
    k = 0
    if n < 10:
        for i in range(1,n):
            if n % i == 0:
                k += 1
    else:
        for i in range(1,int(n/2) + 1):
            if n % i == 0:
                k += 1
    k += 1
    return k
def div(u):
    h = 0
    i = 60
    while (h < u):
        tri = int((i*(i+1))/2)
        # Counting the divisors of tri
        h = countDivisors(tri)
        print(tri, '\t', countDivisors(int(((i-2)*(i-1))/2)))
        i += 1
    print(int(((i-2)*(i-1))/2))
    return tri
print(div(100))

