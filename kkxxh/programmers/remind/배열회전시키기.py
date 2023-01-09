def solution(numbers, direction):
    answer = 0
    if direction == "right":
        answer = [numbers[-1]] + numbers[:len(numbers)-1]
    else:
        answer = numbers[1:] + [numbers[0]]
    return answer


from collections import deque
def solution2(numbers.direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else :
        numbers.rotate(-1)
    return list(numbers)