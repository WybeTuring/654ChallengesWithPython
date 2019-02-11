import time
 
def find_max_palindrome(min=100,max=999):
    max_palindrome = 0
    for a in range(min,max + 1):
        for b in range(a + 1, max + 1): # avoid duplicates
            prod = a*b
            if prod > max_palindrome and str(prod)==(str(prod)[::-1]):
                max_palindrome = prod
    return max_palindrome
 
start = time.time()
L = find_max_palindrome()
elapsed = (time.time() - start)
 
print(L, "in", elapsed, "seconds")