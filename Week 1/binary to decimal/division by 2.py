def decToBinary(n):
    binArr = []
    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //=2
    binArr.reverse()
    return "".join(binArr)
if __name__ == "__main__":
    n = 12
    print(decToBinary(n))