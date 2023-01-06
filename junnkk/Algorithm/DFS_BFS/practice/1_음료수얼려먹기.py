# 다시 풀어보기

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    if x<0 or n>=n or y<0 or y>=m:
        return False
    
    if graph[x][y] ==0 :
        graph[x][y] =1
        
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False


result = 0

for i in range(n):
    for i in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)