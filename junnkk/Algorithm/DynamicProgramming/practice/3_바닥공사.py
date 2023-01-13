n = int(input())

d = [0]*1001


# 탑다운 방식 (메모이제이션, 재귀)
# def floor(x):
#     if x == 1:
#         return 1
#     if x == 2:
#         return 3
#     if d[x] != 0:
#         return d[x]

#     d[x] = floor(x-1) + floor(x-2)*2
#     return d[x]


# print(floor(n) % 796796)


# 보텀업 방식 (DP테이블, 반복)
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] * 2

print(d[n]%796796)
