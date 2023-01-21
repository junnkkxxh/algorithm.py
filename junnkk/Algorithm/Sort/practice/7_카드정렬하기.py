import heapq
n = int(input())

card_nums = []

for _ in range(n):
    heapq.heappush(card_nums, int(input()))

answer = 0
while len(card_nums) > 1:
    temp = heapq.heappop(card_nums)
    temp += heapq.heappop(card_nums)
    answer += temp
    heapq.heappush(card_nums, temp)

print(answer)
