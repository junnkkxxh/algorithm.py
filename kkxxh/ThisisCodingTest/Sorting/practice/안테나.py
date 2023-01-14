N = int(input())
locations = list(map(int,input().split()))
locations.sort()
data= []
for i in range(1,max(locations)+1):
    sum = 0
    for location in locations:
        sum += abs(location-i)
    data.append(sum)
min =min(data)
print(data.index(min)+1)


#답안 예시 = 중간값을 출력하는 것이 답이다
print(locations[(N-1)//2])