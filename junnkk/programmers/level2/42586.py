import math
# from collections import deque


def solution(progresses, speeds):
    answer = []
    temp = []

    progresses = [100-p for p in progresses]

    for i in range(len(progresses)):
        progresses[i] = math.ceil(progresses[i]/speeds[i])

    for i in range(len(progresses)):
        if len(temp) == 0:
            temp.append(progresses[i])
        else:
            if temp[0] < progresses[i]:
                answer.append(len(temp))
                temp = []
                temp.append(progresses[i])
            else:
                temp.append(progresses[i])

    if temp:
        answer.append(len(temp))

    return answer
