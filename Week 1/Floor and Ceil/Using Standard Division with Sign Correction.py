def floorDiv(a,b):
    return a//b
def ceilDiv(a, b):
    return -(-a//b)
def divFloorCeil(a, b):
    res = []
    res.append(floorDiv(a,b))
    res.append(ceilDiv(a,b))
    return res
if __name__ == "__main__":
    a, b = 7, 2
    res = divFloorCeil(a,b)
    print(res[0], res[1])