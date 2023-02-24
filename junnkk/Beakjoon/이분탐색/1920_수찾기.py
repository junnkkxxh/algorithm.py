import sys


def binary_search(array, target, start, end):
    while start <=end:
        mid = (start + end) //2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0
            
    
    

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
target_list = list(map(int, input().split()))


for target in target_list:
    print(binary_search(a,target,0,n-1))

