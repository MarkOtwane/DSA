def gcd(a, b):
    results = min(a,b)
    while results > 0:
        if a % results == 0 and b % results == 0:
            break
        results -= 1
    return results

if __name__ == "__main__":
    a = 20
    b = 28
    print(gcd(a, b))