# 귤 고르기

def solution(k, tangerine):
    answer = 0

    # count -> 시간 초과
    # tangerine_cnt = {t:tangerine.count(t) for t in tangerine}

    # 수정 코드
    tangerine_cnt = {t: 0 for t in tangerine}
    for t in tangerine:
        tangerine_cnt[t] += 1
    ###

    tangerine = sorted(
        tangerine_cnt, key=lambda x: tangerine_cnt[x], reverse=True)

    for i in range(len(tangerine)):
        k -= tangerine_cnt[tangerine[i]]
        answer += 1
        if k <= 0:
            break

    return answer
