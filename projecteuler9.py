def pythagoreanNumb(x,y,z):
    if x**2 + y**2 == z**2:
        return True
    else:
        return False
list1 = []
for i in range(1,1000):
    for j in range(1,i):
        for k in range(1,j):
            if pythagoreanNumb(i,j,k):
                list1.append([i,j,k])
for x in list1:
    if sum(x) == 1000:
        print(x)

