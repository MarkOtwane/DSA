def isEven(n):
    if(n&1)==0:
        return True
    else:
        return False
if __name__ == "__main__":
    n = 14
    if isEven(n):
        print("true")
    else:
        print("false")
#how to print a list of even numbers from 1 to n 