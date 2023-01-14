N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort() # 오름차순
B.sort(reverse=True) #내림차순

for i in range(K):
    if A[i] <B[i]:
        A[i], B[i] = B[i],A[i]
    else : break
# while K != 0:
#     i = 0
#     if A[i] < B[i] :
#         A[i], B[i] = B[i], A[i]
#     else: break
#     i += 1
#     K -= 1
print(sum(A))
