def solution(N, stages):
    
    failure_rate = {}

    stages.sort()

    for i in range(1, N+1):
        total = 0
        failed = 0

        for j in range(len(stages)):
            if i == stages[j]:
                failed += 1
            elif i < stages[j]:
                break

        for j in range(len(stages)):
            if i == stages[j]:
                total = len(stages[j:])
                break

        if total == 0 or failed == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = failed/total

    failure_rate = sorted(
        failure_rate, key=lambda x: failure_rate[x], reverse=True)

    return failure_rate


# 참고 1 -> sort() 사용 안함. count 사용함.
# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)



# 실패 1 (시간 초과)
#     failure_rate = {}

#     stages.sort()

#     for i in range(1,N+1):
#         total = 0
#         failed = 0

#         for j in range(len(stages)):
#             if i<=stages[j]:
#                 total+=1
#             if i == stages[j]:
#                 failed +=1

#         if total == 0 or failed == 0:
#             failure_rate[i] = 0
#         else:
#             failure_rate[i] = failed/total

#     failure_rate = sorted(failure_rate ,key=lambda x:failure_rate[x], reverse = True)

#     return failure_rate
