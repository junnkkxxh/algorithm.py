# 위상 정렬 - deque 이용
# 리스트를 복제할 때는 deepcopy 이용

from collections import deque
# import copy

n = int(input())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in range(1,len(data)-1):
        graph[data[j]].append(i)
        indegree[i] +=1

def topology_sort():
    q = deque()
    # result = copy.deepcopy(time)
    result = [t for t in time]
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1,n+1):
        print(result[i])
        
topology_sort()
        
