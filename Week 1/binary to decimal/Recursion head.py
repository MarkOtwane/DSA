def decToBinaryRec(n, binArr):
    if n == 0:
        return
    
    decToBinaryRec(n//2, binArr)
    binArr.append(str(n % 2))

def decToBinary(n):
    if n == 0:
        return "0"
    
    binArr = []
    decToBinaryRec(n, binArr)
    return "".join(binArr)

if __name__ == "__main__":
    n = 12
    print(decToBinary(n))