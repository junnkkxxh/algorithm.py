def solution(s):
    cnt = 0
    zero_cnt = 0

    while int(s) != 1:
        s_len = len(s)
        s = [i for i in s if int(i) != 0]
        zero_cnt += (s_len - len(s))
        s = str(bin(len(s)))[2:]
        cnt += 1

    return [cnt, zero_cnt]
