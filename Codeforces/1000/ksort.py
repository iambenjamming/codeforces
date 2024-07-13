import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    kdiff = 0
    answer = 0

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            answer += arr[i-1] - arr[i]
            kdiff = max(kdiff, arr[i-1] - arr[i])
            arr[i] = arr[i-1]

    answer += kdiff

    print(answer)
