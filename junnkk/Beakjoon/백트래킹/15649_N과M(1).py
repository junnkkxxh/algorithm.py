# from itertools import permutations

# n,m = map(int, input().split()) 
# n_list = [i+1 for i in range(n)]

# for comb in permutations(n_list, m):
#     for i in range(m):
#         print(comb[i], end=' ')
#     print()


n,m = map(int, input().split()) 

result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()       
    
dfs()
