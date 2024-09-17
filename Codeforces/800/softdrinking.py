n,k,l,c,d,p,nl,np = map(int, input().split())

ml = k*l
limes = c*d

need = n*nl
needsalt = n*np

ans = min(ml//need, limes//n, p//needsalt)

print(ans)