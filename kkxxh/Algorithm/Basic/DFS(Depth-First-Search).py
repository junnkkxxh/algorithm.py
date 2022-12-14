'''
DFS -  깊이 우선 탐색
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
DFS는 스택 구조(혹은 재귀함수)를 이용
<동작과정> 
    1. 탐색 시작 노드를 스택에 삽입하고 방문처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
       방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 더이상 2번의 과정을 수행할 수 없도록
'''

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end='') #해당 노드의 번호 출력
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],#노드가 1부터 시작하는 경우가 많으므로 인덱스 0은 비워둠
    [2,3,8],#노드1의 인접한 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]* 9 #index 0은 사용하지 않음

#정의된 DFS 함수 호출
dfs(graph, 1, visited)

