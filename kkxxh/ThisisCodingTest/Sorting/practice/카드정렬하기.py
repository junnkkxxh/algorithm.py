import heapq

N = int(input())

heap = []
for i in range(N):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) != 1: #heap에 원소가 1개 남을 때 까지
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_ = one+two
    result += sum_
    heapq.heappush(heap,sum_)

print(result)
