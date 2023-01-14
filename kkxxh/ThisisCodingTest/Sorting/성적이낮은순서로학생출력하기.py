N = int(input())

score = []
for i in range(N):
    data = input().split()
    score.append([data[0],int(data[1])])

score = sorted(score,key=lambda score: score[1])
print(score)
for datas in score:
    print(datas[0],end =" ")