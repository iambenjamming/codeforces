o = input()
hashmap = {}

prefixbal = [0] * (len(o)+1)
balance = 0

for i in range(len(o)):
    if o[i] == '(':
        balance += 1
    elif o[i] == ')':
        balance -= 1
    prefixbal[i+1] = balance

prefixbal.pop()

hashmap = dict(enumerate(prefixbal))

new = dict(sorted(hashmap.items(), key = lambda x: (x[1], -x[0])))

ans = []
for key in new:
    ans.append(o[key])

print(''.join(ans))
