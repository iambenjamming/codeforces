x = input()
digits = [int(digit) for digit in x]
ans = []


if digits[0] != 9:
    for num in digits:
        if num > 4:
            answer = 9 - num
            ans.append(answer)
            continue
        ans.append(num)
else:
    ans.append(9)
    for i in range(1, len(digits)):
        if digits[i] > 4:
            answer = 9 - digits[i]
            ans.append(answer)
            continue
        ans.append(digits[i])

real = ''.join(map(str, ans))
print(int(real))

