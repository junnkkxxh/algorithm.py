import sys

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

def binary_search(array, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif mid > array[mid] :
            start = mid + 1
        else:
            end = mid - 1
               
    return -1
            
print(binary_search(n_list, 0,len(n_list)-1))
