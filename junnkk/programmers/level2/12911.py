def solution(n):
    n_bin_cnt = 0
    answer = n
    ans_bin_cnt = 0

    n_list = list(bin(n))
    for i in range(2, len(n_list)):
        if n_list[i] == '1':
            n_bin_cnt += 1

    print(n_bin_cnt)

    while ans_bin_cnt != n_bin_cnt:

        answer += 1
        ans_bin_cnt = 0

        ans_list = list(bin(answer))
        for i in range(2, len(ans_list)):
            if ans_list[i] == '1':
                ans_bin_cnt += 1

    return answer
