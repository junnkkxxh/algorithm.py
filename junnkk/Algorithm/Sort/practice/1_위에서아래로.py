n = int(input())

nums = []

for _ in range(n):
    nums.append(input())

for num in sorted(nums, reverse=True):
    print(num, end=' ')
