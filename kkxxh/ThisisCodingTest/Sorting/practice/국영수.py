N= int(input())
student = []
for i in range(N):
    data = list(input().split())
    student.append([data[0],int(data[1]),int(data[2]),int(data[3])])

student = sorted(student,key=lambda student :( -student[1], +student[2], -student[3], student[0]))

print(student)
for i in student:
    print(i[0],end=" ")