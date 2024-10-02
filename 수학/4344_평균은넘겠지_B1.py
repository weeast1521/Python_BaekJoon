C = int(input())

for _ in range(C):
    student = list(map(int,input().split()))

    average = sum(student[1:]) / student[0]
    count = 0

    for i in range(1,student[0]+1):
        if student[i] > average:
            count += 1
    
    print("%0.3f%%"%((count/student[0])*100))