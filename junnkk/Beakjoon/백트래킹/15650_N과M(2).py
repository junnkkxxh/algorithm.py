# from itertools import combinations

# n,m = map(int, input().split()) 
# n_list = [i+1 for i in range(n)]

# for comb in combinations(n_list, m):
#     for i in range(m):
#         print(comb[i], end=' ')
#     print()


n,m = map(int, input().split()) 

result = []
idx = 1

def dfs(idx):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(idx,n+1):
        if i not in result:
            result.append(i)
            idx +=1
            dfs(idx)
            result.pop()
            
    
dfs(idx)
