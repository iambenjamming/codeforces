a, b = map(int, input().split())

ans = []

ans.append(min(a,b))

used = (max(a,b)-min(a,b))//2
ans.append(used)

print(*ans)