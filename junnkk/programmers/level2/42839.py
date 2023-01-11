from itertools import permutations

def solution(numbers):

    num_list = list(numbers)
    cnt = 0
    temp = []

    for i in range(1, len(num_list)+1):
        perm_list = list(permutations(num_list, i))
        for j in range(len(perm_list)):
            temp.append(int(''.join(perm_list[j])))

    temp = list(set(temp))

    for i in range(len(temp)):
        if temp[i] <= 1:
            continue
        cnt += 1
        for j in range(2, temp[i]):
            if temp[i] % j == 0:
                cnt -= 1
                break

    return cnt
