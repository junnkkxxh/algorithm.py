N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
num.sort(reverse=True )
print(num)