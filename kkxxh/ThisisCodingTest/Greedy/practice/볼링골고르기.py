N, M = map(int,input().split())
weight = list(map(int,input().split()))

def sol1(N,M,weight):
    answer = 0
    for i in range(N):
        for j in range(N):
            if weight[i] != weight[j] and i != j and i<j:
                answer+=1

    return answer

def sol2(N,M,weight):
    array= [0] * 11 #1부터 10까지의 무게를 담을 수 있는 리스트
    for x in weight:
        array[x] +=1
    answer = 0
    for i in range(1,M+1):
        N -= array[i]
        answer += array[i] * N
    return answer