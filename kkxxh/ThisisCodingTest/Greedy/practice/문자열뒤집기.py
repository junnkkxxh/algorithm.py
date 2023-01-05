s = input()

count0 = 0 #전부0으로 바꾸는 경우
count1 = 0 #전부1로 바꾸는 경우

if s[0] == '1':
    count0 += 1
else : count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] =='1':
            count0 +=1
        else: count1 += 1

answer = count0 if count0<count1 else count1
print(answer)