# junnkk

# n = int(input())
# n_list = list(map(int, input().split()))

# m = int(input())
# m_list = list(map(int, input().split()))

# answer = []

# for ml in m_list:
#     if ml in n_list:
#         answer.append('yes')
#     else:
#         answer.append('no')

# for a in answer:
#     print(a, end=(' '))


######################################################
# 이진 탐색을 이용한 방법

def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

    # while start <=end:
    #     mid = (start+end) //2
    #     if array[mid] == target:
    #         return mid
    #     elif array[mid]>target:
    #         end = mid -1
    #     else:
    #         start = mid +1

    # return None


n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for ml in m_list:
    if binary_search(n_list, ml, 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')


# 이진 탐색 or 게수 정렬 or set을 이용하여 문제 풀이 가능
