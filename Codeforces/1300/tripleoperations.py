ma=200001
f=[0]
a=[0]*ma

for i in range(1,ma):
    a[i]=a[i//3]+1
    f.append(f[-1]+a[i])
 
t = int(input())

for _ in range(t):
    l, r = map(int,input().split())
    
    print(f[r]-f[l-1]+a[l])
