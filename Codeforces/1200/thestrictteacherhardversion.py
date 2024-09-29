import bisect

t = int(input())

for _ in range(t):
    n, m, q = map(int, input().split())
    teachers = list(map(int, input().split()))
    teachers.sort()
    davids = list(map(int, input().split()))

    for d in davids:

        if d > teachers[-1]:
            print(n-teachers[-1])
            continue
        elif d < teachers[0]:
            print(teachers[0]-1)
        else:
            index = bisect.bisect(teachers, d)
            t1 = teachers[index-1]
            t2 = teachers[index]

            print((t2-t1)//2)