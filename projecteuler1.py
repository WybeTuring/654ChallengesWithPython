<<<<<<< HEAD
#First question in project euler
#This function determines the list of multiples of y and c, and calculates their sum.
def multiplesOfY(x,y,c):
    multiples = []
    answer = 0
    i = 0
    j = 0
    while i < x:
        if i>=y:
            if i%y ==0:
                multiples.append(i)
                i = i+1
            else:
                i = i+1
        else:
            i = i+1
    while j <x:
        if j>=c:
            if (j%c == 0) and not (j in multiples):
                multiples.append(j)
                j = j+1
            else:
                j = j+1
        else:
            j = j+1

    for i in range(0,len(multiples)):
        answer = answer + multiples[i]
    return answer
print(multiplesOfY(1000,3,5))
=======
#First question in project euler
#This function determines the list of multiples of y and c, and calculates their sum.
def multiplesOfY(x,y,c):
    multiples = []
    answer = 0
    i = 0
    j = 0
    while i < x:
        if i>=y:
            if i%y ==0:
                multiples.append(i)
                i = i+1
            else:
                i = i+1
        else:
            i = i+1
    while j <x:
        if j>=c:
            if (j%c == 0) and not (j in multiples):
                multiples.append(j)
                j = j+1
            else:
                j = j+1
        else:
            j = j+1

    for i in range(0,len(multiples)):
        answer = answer + multiples[i]
    return answer
print(multiplesOfY(1000,3,5))
>>>>>>> origin/master
