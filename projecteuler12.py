# The N-th triangular number is given by n(n+1)/2
i = 150
p = 1
while p<500:
    div =[1]
    n = (i*(i+1))/2
    #find a list of the divisors of n
    for i in range(2,(n//2)+1):
        if n%i == 0:
            div.append(i)
    div.append(n)
    p = len(div)
    i += 1
print(n)