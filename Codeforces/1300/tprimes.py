#sieve of erastothenes
N = 10**6
prime = [1] * (N + 2)
prime[0] = prime[1] = 0

for i in range(2, int(N**0.5) + 1):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = 0

def plswork(k):
    if k < 4:
        return False
    sq = int(k**0.5)
    return sq * sq == k and prime[sq]

n = int(input())
a = list(map(int, input().split()))

for e in a:
    print("YES" if plswork(e) else "NO")
