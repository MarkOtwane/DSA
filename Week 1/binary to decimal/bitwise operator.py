def decToBinary(n):
    bin = ""

    while n>0:

        bit = n & 1

        bin += str(bit)
        n = n>>1
    return bin[::-1]
    
if __name__ == "__main__":
    n =12
    print(decToBinary(n))
    # bitwise method is faster and efficient