n = 2**1000
nstr = str(n)
sum = 0
for i in range(0,len(nstr)):
    sum += int(nstr[i])
print(sum)
