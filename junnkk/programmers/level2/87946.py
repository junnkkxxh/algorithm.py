from itertools import permutations


def solution(k, dungeons):
    answer = 0

    dungeons_perm_list = list(permutations(dungeons, len(dungeons)))

    for dungeons in dungeons_perm_list:
        cnt = 0
        temp = k
        for d in dungeons:
            if temp >= d[0]:
                temp -= d[1]
                cnt += 1
            else:
                break
            if cnt == len(dungeons):
                return cnt
        answer = max(answer, cnt)

    return answer
