def solution(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return b % 1234567
