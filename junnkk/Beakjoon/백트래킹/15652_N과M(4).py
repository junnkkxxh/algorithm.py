n,m = map(int, input().split()) 

result = []
idx = 1
def dfs(idx):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(idx,n+1):
        result.append(i)
        dfs(idx)
        idx += 1
        result.pop()
            
    
dfs(idx)