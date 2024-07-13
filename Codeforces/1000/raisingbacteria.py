n = int(input())

binary = bin(n)

listbin = list(binary[2:])

print(listbin.count('1'))