n = int(input())

student_info = []

for _ in range(n):
    data = input().split()
    student_info.append((data[0], int(data[1])))

student_info.sort(key=lambda x: x[1])

for i in range(n):
    print(student_info[i][0])
