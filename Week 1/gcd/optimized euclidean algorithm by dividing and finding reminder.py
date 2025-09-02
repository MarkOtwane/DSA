def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
a = 20
b = 30
print(gcd(a, b))