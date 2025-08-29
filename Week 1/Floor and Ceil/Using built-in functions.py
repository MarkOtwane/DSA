import math
def divFloorCeil(a, b):
    floor_val  = math.floor(a/b)
    ceil_val = math.ceil(a/b)
    return [floor_val, ceil_val]
if __name__ == "__main__":
    a, b = 1, 2
    res = divFloorCeil(a, b)
    print(res[0], res[1])