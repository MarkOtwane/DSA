def divBy13(s):
    num = int(s)
    return num % 13 == 0
if __name__ == "__main__":
    s = "2911281"
    isDivisible = divBy13(s)
    if isDivisible:
        print('true')
    else:
        print('false')