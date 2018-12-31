<<<<<<< HEAD
# This function determines if a number devides all the elements of a list
def groupdivisor(num, group):
    for x in group:
        if num % x != 0:
            return 0
    return 1
list2 = [x for x in range(1,21)]
print(list2)
number = 2520
while groupdivisor(number, list2) == 0:
    number = number + 20
print(number)
=======
# This function determines if a number devides all the elements of a list
def groupdivisor(num, group):
    for x in group:
        if num % x != 0:
            return 0
    return 1
list2 = [x for x in range(1,21)]
print(list2)
number = 2520
while groupdivisor(number, list2) == 0:
    number = number + 20
print(number)
>>>>>>> origin/master
