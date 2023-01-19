# 다익스트라
import heapq

INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

cnt = -1
total_time = 0

for d in distance:
    if d != INF:
        cnt += 1
        total_time = max(total_time, d)


print(cnt, total_time)


# # 플로이드 워셜 --> n의 범위가 크기 때문에 사용 X

# INF = int(1e9)

# n, m, c = map(int, input().split())
# graph = [[INF]*(n+1) for _ in range(n+1)]

# print(graph)

# for _ in range(m):
#     x, y, z = map(int,input().split())
#     graph[x][y] = z
