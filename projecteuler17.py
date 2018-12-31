def wordcount(x):
    if x == 1 or x == 2 or x == 6 or x == 10:
        return 3
    elif x == 4 or x == 5 or x == 9:
        return 4
    elif x == 3 or x == 7 or x == 8:
        return 5
    elif len(str(x)) == 2:
        if x == 11 or x == 12 or x == 20 or x == 30 or x == 80 or x == 90:
            return 6
        elif x == 40 or x == 50 or x == 60:
            return 5
        elif x == 13 or x == 14 or x == 18 or x == 19:
            return 8
        elif x == 15 or x == 16 or x == 70:
            return 7
        elif x == 17:
            return 9
        else:
            i = x//10
            j = x % 10
            return (wordcount(i*10) + wordcount(j))
    elif x == 1000:
        return 11
    else:
        if x%100 == 0:
            return (wordcount(x//100) + 7)
        else:
            return (wordcount(x//100) + 10 + wordcount(x%100))
sum = 0
for i in range(1,1001):
    sum += wordcount(i)
print(sum)
