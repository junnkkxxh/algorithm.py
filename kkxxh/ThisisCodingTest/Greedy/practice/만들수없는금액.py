N = int(input())
money = list(map(int,input().split()))

money.sort(reverse=False)

check = 1
for i in money:
    if check < i :
        break
    check += i

print(check)