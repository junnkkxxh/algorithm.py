def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr :
        if i %divisor ==0 :
            answer.append(i)
    if answer == []:
        answer = [-1]
    return answer