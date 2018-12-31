numbers = [x for x in range(1,101)]
numbersSum = sum(numbers)
numbersSquare = [x**2 for x in numbers]
ans = numbersSum**2 - sum(numbersSquare)
print(ans)