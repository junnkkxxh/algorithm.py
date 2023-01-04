num = input()

num_list = [int(i) for i in num]

answer = 0
for i in num_list :
    if i <= 1 or answer <= 1 :
        answer += i
    else : 
        answer *= i

print(answer)