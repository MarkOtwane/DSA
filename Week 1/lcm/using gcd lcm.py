def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
def lcm(a, b):
    return (a // gcd(a, b))*b
if __name__ == "__main__":
    a = 12
    b = 14
    print(lcm(a, b))