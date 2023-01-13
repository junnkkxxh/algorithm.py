n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(coins[i], m+1):
        d[j] = min(d[j], d[j-coins[i]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
 