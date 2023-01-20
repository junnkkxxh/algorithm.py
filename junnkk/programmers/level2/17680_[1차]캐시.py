# [1차] 캐시

from collections import deque


def solution(cacheSize, cities):
    answer = 0

    cache = deque()

    for city in cities:
        city = city.capitalize()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
            answer += 5

    return answer


# 참고
# deque의 maxlen


# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time
