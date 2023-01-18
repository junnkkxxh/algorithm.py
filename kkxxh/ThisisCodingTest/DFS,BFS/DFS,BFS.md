DFS/BFS - 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

REMIND
탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

스택, 큐
- 삽입(push) : 데이터를 삽입
- 삭제(pop) : 데이터를 삭제

스택 : 선입 후출, 박스 쌓기
    .append()
    .pop()
큐 : 선입 선출, 대기 줄

파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료 구조 활용할 것
from collections import deque
deque = 스택과 큐의 장점 모두 채택



그래프 
- 노드(Node,Vertex)
- 간선(Edge)

그래프 표현법
- 인접 행렬(Adjacency Matrix) : 2차원 배열에 각 노드가 연결된 형태를 저장(표 형식), 연결이 되지 않은 노드끼리 Infinity로 작성
    INF = 99999999
    graph = [
        [0,7,5],
        [7,0,INF],
        [5,INF,0]
    ]
- 인접 리스트(qAdjacency List)
    graph = [[] for _ in range(3)]
    graph[0].append((1,7))
    graph[0].append((2,5))

    graph[1].append((0,7))
    
    graph[2].append((0,5))

메모리 측면에서 보면 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비
인접 리스트 방식은 인접 행렬 방식에 비해 속도가 느리다

DFS (depth-first search) : 깊이 우선 탐색 (그래프의 깊은 부분을 우선적으로 탐색)
(스택 사용)
1) 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다
2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
3) 2)번 과정을 더 이상 수행할 수 없을 때 까지 반복

DFS.py
    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=" )
        for i in graph[v]:
            if not visited[i]:
                dfs(graph,i,visited)
    graph = [~~~]
    visited = [False] * 9
    dfs(graph,1,visited)



BFS (Breadth First Search) : 너비 우선 탐색 - 가까운 노드부터 탐색
( 큐 이용 )
1) 탐색 시작 노드를 큐에 삽입하고 방문 처리한다
2) 큐에서 노드를 꺼내 해당 노드와 인접 노드 중에서 방문하지 않은 모든 노드를 모두 큐에 삽입한다
3) 2)번 과정을 더 이상 수행할 수 없을 때 까지 반복

BFS.py
    from collections import deque
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            v= queue.popleft()
            print(v, end="")
            for i in graph[v]:
                if not visited[i] :
                    queue.append(i)
                    visited[i] = True

    graph = [~~~]
    visited = [False]*9
    bfs(graph,1,visited)