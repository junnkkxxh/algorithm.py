# 모음 사전 # 완전탐색

from itertools import product

def solution(word):
    
    words = []
    
    for i in range(1,6):
        for j in product(['A','E','I','O','U'],repeat=i):
            words.append(''.join(list(j)))
        
    return sorted(words).index(word)+1