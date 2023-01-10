def solution(brown, yellow):
    x = 0
    y = 0

    total = brown + yellow
    for i in range(1, brown):
        y = i
        x = (brown+4)/2-y
        if x * y == total:
            break
    answer = [x, y]
    return answer
