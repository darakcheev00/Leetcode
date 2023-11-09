def sumDigits(s):
    total = 0

    while len(s):
        c = s[-1]
        total += int(c)
        s = s[:-1]
        
    return str(total)

def superDigit(n, k):
    # Write your code here
    n = int(sumDigits(n))
    n *= k
    n = str(n)
    
    while len(n) > 1:
        n = sumDigits(n)
        
    return int(n)

print(superDigit("9875", 4))