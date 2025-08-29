def isEven(n):
    rem = n%2
    if rem == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    n = 23
    if isEven(n):
        print("true")
    else:
        print("false")