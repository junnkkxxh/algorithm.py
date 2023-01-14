N = int(input())
stages = list(map(int,input().split()))

count = [] * (N+1)

for stage in stages:
    if stage > N : break
    for i in range(stage):
        count[i][0] += 1

for i in range(count):
    if i ==len(count):
        try_game = count[i] 
        fail_game = 0
        count[i][1] = fail_game/try_game
    else : 
        try_game = count[i]
        fail_game = count[i]-count[i+1]
        count[i][1] = fail_game/try_game
        
count = sorted(count,key=lambda count: -count[1])

for i in count:
    print(i[0],end=" ")