s = input()

length = len(set(s))

if length&1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')