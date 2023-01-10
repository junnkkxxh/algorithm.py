def solution(prices):


    return answer




# 실패 1 
# 완전 탐색 
# -> tc는 모두 통과하였으나 효율성에서 fail
# 
# def solution(prices):
    
#     answer = [0 for _ in range(len(prices))]

#     for i in range(0, len(prices)-1):
#         for j, p in enumerate(prices[i+1:]):
#             if p < prices[i]:
#                 answer[i] = j+1
#                 break
#         if answer[i] == 0:
#             answer[i] = len(prices) - i-1

#     return answer
