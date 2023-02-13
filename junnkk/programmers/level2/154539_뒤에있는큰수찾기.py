
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



# # stack
# def solution(numbers):
#     stack = []
#     answer = [0] * len(numbers)

#     for i in range(len(numbers)):
#             while stack and numbers[stack[-1]] < numbers[i]:
#                 answer[stack.pop()] = numbers[i]
#             stack.append(i)
#     while stack:
#             answer[stack.pop()] = -1
    
#     return answer


# 우선순위 큐
import heapq

def solution(numbers):
    answer = [-1] * len(numbers) 
    h = []
    
    for i, n in enumerate(numbers):
        while h and h[0][0]< n:
            _, idx = heapq.heappop(h)
            answer[idx] = n
        heapq.heappush(h,(n,i))
        
        
        
            
                              
    return answer
