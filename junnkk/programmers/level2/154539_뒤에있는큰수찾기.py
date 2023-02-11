
# 실패 -> tc 시간 초과
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        if i == len(numbers)-1:
            answer.append(-1)
        for j in range(i+1,len(numbers)):
            if numbers[i] <numbers[j]:
                answer.append(numbers[j])
                break
            if j == len(numbers)-1:
                answer.append(-1)
                              
    return answer