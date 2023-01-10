def solution(n):
    a, b = 0, 1
    if n == 0 or n == 1:
        return n
    for _ in range(n):
        a, b = b, a+b

    return a % 1234567
