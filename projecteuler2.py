<<<<<<< HEAD
#Project two of the project Euler problems
#This function determines the fibonnaci number of rank x
def fibonacci(x):
    fib = [1,2]
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        y = fibonacci(x-1) + fibonacci(x-2)
        return y
#This section of the code creates a list of fibonnaci numbers that are less than four million

j = 0
i = 1
list = []
while i>0 and j == 0:
    if fibonacci(i) <= 4000000:
        list.append(fibonacci(i))
        i = i + 1
    else:
        j = 1
#Summing the even fibonnaci numbers
sum = 0
for i in range(0,len(list)):
    if list[i]%2 == 0:
        sum = sum + list[i]
print(sum)
=======
#Project two of the project Euler problems
#This function determines the fibonnaci number of rank x
def fibonacci(x):
    fib = [1,2]
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        y = fibonacci(x-1) + fibonacci(x-2)
        return y
#This section of the code creates a list of fibonnaci numbers that are less than four million

j = 0
i = 1
list = []
while i>0 and j == 0:
    if fibonacci(i) <= 4000000:
        list.append(fibonacci(i))
        i = i + 1
    else:
        j = 1
#Summing the even fibonnaci numbers
sum = 0
for i in range(0,len(list)):
    if list[i]%2 == 0:
        sum = sum + list[i]
print(sum)
>>>>>>> origin/master
