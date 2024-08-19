nums = list(input().split('+'))

nums.sort()

ans = ''

ans += nums[0]

for i in range(1, len(nums)):
    ans += '+' + nums[i]

print(ans)
