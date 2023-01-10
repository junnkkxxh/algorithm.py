def solution(numbers):

    numbers = list(map(str, numbers))
    # print(numbers)
    numbers.sort(key=lambda x: x*3, reverse=True)
    # print(numbers)

    return str(int(''.join(numbers)))


# 실패1 -> 시간 초과
# from itertools import permutations

# def solution(numbers):
#     answer = ''

#     permutation = list(permutations(numbers))
#     temp = []
#     for p in permutation:
#         s = ""
#         for i in p:
#             s +=str(i)
#         temp.append(int(s))

#     return str(max(temp))
