try:
    x = int(input())
    x = int(x)
    five = x // 5
    x = x - (five * 5)
    two = x // 2
    x = x - (two * 2)
    one = x // 1
    print("5 -",five)
    print("2 -",two)
    print("1 -",one)

except ValueError:
    print("error")
