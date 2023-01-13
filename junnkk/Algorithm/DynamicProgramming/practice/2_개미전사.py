n = int(input())

foods = list(map(int, input().split()))

d = [0] * 101


# 탑다운 방식 (메모이제이션, 재귀)
def max_food(x):
    if x == 0:
        return foods[0]
    if x == 1:
        return max(foods[0], foods[1])
    if d[x] != 0:
        return d[x]

    d[x] = max(max_food(x-1), max_food(x-2) + foods[x])
    return d[x]


print(max_food(n-1))




# 보텀업 방식 (DP테이블, 반복)
# d[0] = foods[0]
# d[1] = max(foods[0], foods[1])


# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2]+foods[i])

# print(d[n-1])
