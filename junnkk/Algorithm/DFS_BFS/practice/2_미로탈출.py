# 다시 풀어보기

from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

result = 0

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))


# from collections import deque

# n, m = map(int, input().split())

# graph = []

# for _ in range(n):
#     graph.append(list(map(int, input())))


# def bfs(graph, x,y):
#     result = 0

#     queue = deque((x,y))

#     while queue:
#         x,y = queue.popleft()

#         graph[x-1][y-1] = 0

