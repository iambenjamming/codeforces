def guess(num):

    bredneed = (bredreq * num)
    sausneed = (sausreq * num)
    chesneed = (chesreq * num)

    bredbuy = max(0, bredneed - bredinv)
    sausbuy = max(0, sausneed - sausinv)
    chesbuy = max(0, chesneed - chesinv)

    moneyreq = bredbuy*bredcost + sausbuy*sauscost + chesbuy*chescost

    oneburbur =  (bredcost*bredreq) + (sauscost*sausreq) + (chescost*chesreq)

    return moneyreq <= wallet

recipe = input()

bredinv, sausinv, chesinv = map(int, input().split())
bredcost, sauscost, chescost = map(int, input().split())

wallet = int(input())

bredreq = recipe.count('B')
if bredreq == 0: bredinv = 0
sausreq = recipe.count('S')
if sausreq == 0: sausinv = 0
chesreq = recipe.count('C')
if chesreq == 0: chesinv = 0

left = 0
right = 10**99

while left < right:
    mid = (left + right + 1) // 2
    if guess(mid):
        left = mid
    else:
        right = mid - 1

print(left)
