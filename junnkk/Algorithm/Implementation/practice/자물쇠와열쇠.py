def solution(key, lock):

    # lock = [
    #     [1,1,1,1,1],
    #     [1,1,0,1,1],
    #     [1,0,1,1,1],
    #     [1,1,1,1,1],
    #     [1,1,0,0,1],
    # ]

    min_column, max_column = 21, 0
    min_row, max_row = 21, 0

    for i in range(len(lock)):
        if 0 in lock[i]:
            min_column = min(min_column, i)
            max_column = max(max_column, i)
            for j in range(len(lock[i])):
                if lock[i][j] == 0:
                    min_row = min(min_row, j)
                    max_row = max(max_row, j)

    new_lock = [lock[i][min_row:max_row+1]
                for i in range(min_column, max_column+1)]
    print(new_lock)

    print(min_column, max_column)
    print(min_row, max_row)

    if max(len(new_lock), len(new_lock[0])) > max(len(key), len(key[0])):
        print(max(len(new_lock), len(new_lock[0])))
        print(max(len(key), len(key[0])))
        return False

    # for i in range():

    # min_row = min([i for i in range()])
    # max_row = max([])
    # min_column = min([j for i in range() for j in range() if ])
    # max_column = max([])
    answer = True

    return answer
