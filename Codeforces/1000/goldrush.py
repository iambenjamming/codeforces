import sys

def split(n, m):

    if n == m:
        return True
    if n % 3 != 0  or m > n:
        return False

    x = n / 3
    bigger = 2 * x

    return split(bigger, m) or split(x, m)

t = int(sys.stdin.readline())

for _ in range(t):

    nm = sys.stdin.readline().split()
    n = int(nm[0])
    m = int(nm[1])

    if split(n, m):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
    
