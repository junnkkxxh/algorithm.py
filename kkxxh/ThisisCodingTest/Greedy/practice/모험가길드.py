N = int(input())
num_list = list(map(int,input().split()))

num_list.sort()

group = 0

people = 0

for i in num_list: 
    people += 1   
    if i <= people:
        group += 1
        people = 0



print(group)    