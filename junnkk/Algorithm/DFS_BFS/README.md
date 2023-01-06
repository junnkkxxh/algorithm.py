## 꼭 필요한 자료구조 기초

 #### 탐색 Search
  : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

 #### 자료구조 Data Structure
  : 데이터를 표현하고 관리하고 처리하기 위한 구조 <br>
   그 중 stack과 queue는 자료구조의 기초 개념으로 다음 두 핵심적인 함수로 구성된다.

   > 삽입(push) 
   > 삭제(pop)
 
  ###### overflow & underflow
 
 <br>
 
 ### 스택 Stack
  - 선입후출(**F**irst **I**n **L**ast **O**ut) - 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조
  - 입구와 출구가 동일한 형태로 스택을 시각화
  
          
  ``` python
  stack = []

  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()
  
  print(stack[::-1])  # 최상단 원소부터 출력 [1,3,2,5]
  print(stack)  # 최하단 원소부터 출력 [5,2,3,1]
  ```
  -> append() 메서드는 리스트의 가장 뒤쪽에 데이터를 삽입하고, pop() 메서드는 리스트의 가장 뒤쪽에서 데이터를 꺼낸다.

  <br>
  <br>
 
 ### 큐 Queue
  - 선입선출(**F**irst **I**n **F**irst **O**ut) - 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조
  - 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 
      
  ``` python 
  from collections import deque
  
  # 큐(Queue)는 구현을 위해 deque 라이브러리 사용
  queue  = deque()
  
  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()
  queue.append(1)
  queue.append(4)
  queue.popleft()
  
  print(queue)  # 먼저 들어온 순서대로 출력 [3,7,1,4]
  queue.reverse()  # 역순으로 바꾸기
  print(queue)  # 나중에 들어온 원소부터 출력 [4,1,7,3]
  ```
  -> deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.

  <br>

 ### 재귀 함수 Recursive Function
  - 자기 자신을 다시 호출하는 함수
  - 입구와 출구가 동일한 형태로 스택을 시각화
  <br>
  <br>

## 탐색 알고리즘 DFS/BFS

 #### 그래프의 기본 구조 및 표현 방식
  - 노드 Node = 정점 Vertex
  - 간선 Edge
  
  > 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다.
  > 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다(Adjacent)'라고 표현한다.

  <br> 

  ##### 인접 행렬(Adjacency Matrix)
  : 2차원 배열에 그래프의 연결 관계를 표현하는 방식 = 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식<br>
  연결되어 있지 않는 노드끼리는 무한의 비용이라고 작성한다. ex) 1e9
      
  ``` python
  INF = 1e9 # 무한의 비용 선언

  # 2차원 리스트를 이용해 인접 행렬 표현
  graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
  ]

  print(graph) # [[0, 7, 5], [7, 0, INF], [5, INF, 0]]
  ```
  
  
  ##### 인접 리스트(Adjacency List)
  : 리스트로 그래프의 연결 관계를 표현하는 방식 
  > 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
      
  ``` python
  # 행(row)이 3개인 2차원 리스트로 인접 리스트 표현 
  graph = [[] for _ in range(3)]

  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1, 7))
  graph[0].append((2, 5))

  # 노드 1에 연결된 노드 정보 저장(노드, 거리)
  graph[1].append((0, 7))

  # 노드 2에 연결된 노드 정보 저장(노드, 거리)
  graph[2].append((0, 5))

  print(graph) # [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
  ```
  <br>
  <br>

  > 두 방식의 차이 
  > - 인접 행렬 방식은 모든 관계를 저장하기 때문에 노드 개수가 많으면 메모리가 불필요하게 낭비된다.
  > - 인접 리스트 방식은 연결된 정보만 저장하므로 메모리를 효율적으로 사용하나, 특정한 두 노드가 연결되는지에 대한 정보를 얻는 속도가 느리다.(연결된 데이터를 하나하나 확인해야 하므로)

  <br>
  <br>



 ### 깊이 우선 탐색 DFS(Depth-First Search)
  : 그래프의 깊은 부분은 우선적으로 탐색하는 알고리즘 
  \- 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘
  - 스택 자료 구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다. 
  >1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  > 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  > 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
  

  <br>

  - 실제로는 스택을 사용하지 않아도 되며 탐색을 수행함에 있어서 데이터의 개수가 N인 경우 O(N)의 시간이 소요된다.


  - DFS 예시 
    `방문 기준 : 번호가 낮은 인접 노드부터`<br>
    탐색 순서 : 1 → 2 → 7 → 6 → 8 → 3 → 4 → 5

        
    ``` python
    # DFS 메서드 정의 
    def dfs(graph, v, visited):
        # 현재 노드를 방문처리
        visited[v] = True
        print(v, end=' ')
        # 현재 노드 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)
        
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    graph = [
    	[],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * 9

    # 정의된 DFS 함수 호출 
    dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5
    ``` 
    
 ### 너비 우선 탐색 BFS(Breadth-First Search)
  : 가까운 노드부터 탐색하는 알고리즘 
  - 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다. 
  > 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  > 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
  > 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
  
  <br>

  - 실제로 구현함에 있어 앞서 언급한 대로 deque 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N)의 시간이 소요된다. 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다. 

  - BFS 예시 
    `방문 기준 : 번호가 낮은 인접 노드부터`<br>
    탐색 순서 : 1 → 2 → 3 → 8 → 7 → 4 → 5 → 6

        
    ``` python
    from collections import deque

    # BFS 메서드 정의 
    def bfs(graph, start, visited):
        # 큐 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        # 현재 노드를 방문 처리
        visited[start] = True
        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력
            v = queue.popleft()
            print(v, end=' ')
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        
        
        
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    graph = [
    	[],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * 9

    # 정의된 BFS 함수 호출 
    bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
    ``` 
