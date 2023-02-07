from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = []
distance = [-1] * (n+1)

queue = deque([x])
distance[x] = 0
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            queue.append(i)
            distance[i] = distance[v]+1
            if distance[i] == k:
                result.append(i)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r)
