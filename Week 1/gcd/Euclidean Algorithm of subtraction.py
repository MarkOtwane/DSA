#the gcd of 2 numbers does not change if the smaller  number is subtracted from the bigger number. It is a process of repeat subtraction carrying the result forwaird each time until the result is equal to one number being subtracted

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)
if __name__ == "__main__":
    a = 20
    b = 28
    print(gcd(a, b))