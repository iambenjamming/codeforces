n = int(input())

if n > 9223372036854775807:
    print('BigInteger')
elif n > 2147483647:
    print('long')
elif n > 32767:
    print('int')
elif n > 127:
    print('short')
else:
    print('byte')