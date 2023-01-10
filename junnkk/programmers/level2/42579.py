def solution(genres, plays):
    answer = []

    d = dict()
    genre_total = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in d:
            d[genre] = [(i, play)]
            genre_total[genre] = play
        else:
            d[genre] += [(i, play)]
            genre_total[genre] += play

    genre_total = sorted(
        genre_total, key=lambda x: genre_total[x], reverse=True)

    for g in genre_total:
        temp = sorted(d[g], key=lambda x: x[1], reverse=True)
        answer.append(temp[0][0])
        if len(d[g]) > 1:
            answer.append(temp[1][0])

    return answer
