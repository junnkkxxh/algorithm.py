def solution(s):
    n = 1
    min_len = len(s)

    while n <= len(s)//2:
        n_s = ''
        temp = s[0:n]
        cnt = 1

        for i in range(n, len(s)-n+1, n):
            if temp == s[i:i+n]:
                cnt += 1
            else:
                if cnt == 1:
                    n_s += temp
                else:
                    n_s += str(cnt)+temp

                temp = s[i:i+n]
                cnt = 1

        if cnt == 1:
            n_s += temp
        else:
            n_s += str(cnt)+temp

        if len(s) % n != 0:
            n_s += s[-(len(s) % n):]

        min_len = min(min_len, len(n_s))
        n += 1

    return min_len
