def solution(n, words):
    cnt = 1
    num = 0
    fin = [words[0]]

    for i in range(1, len(words)):
        if i % n == 0:
            cnt += 1

        if words[i-1][-1] != words[i][0]:
            num = i % n+1
            break

        if words[i] in fin:
            num = i % n+1
            break

        fin.append(words[i])

    answer = [num, cnt]
    if num == 0:
        answer = [0, 0]
    return answer
