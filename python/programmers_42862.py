def solution(n, lost, reserve):
    cnt = 0
    student = [1 for _ in range(n)]
    
    for i in lost:
        student[i-1] -=1
    
    for i in reserve:
        student[i-1] += 1
    # student.sort(reverse = True)
    print(student)
    
    for i in range(n):
        if student[i] > 1:
            front, back = i - 1, i + 1
            
            if 0 <= front < n and student[front] == 0:
                student[i] -= 1
                student[front] += 1
            elif 0 <= back < n and student[back] == 0:
                student[i] -= 1
                student[back] += 1
        # if student[i-1] >= 1:
        #     student[i-1] -= 1
        #     student[i] += 1

    print(student)
        
        
#     for i in lost:
#         if i in reserve:
#             lost.remove(i)
#             reserve.remove(i)
            
#     for i in sorted(lost):
#         if i-1 in reserve:
#             reserve.remove(i-1)
#             cnt += 1
#         elif i+1 in reserve:
#             reserve.remove(i+1)
#             cnt += 1

    print(student.count(0))
    #answer = n - (len(lost)-cnt)
    answer = n - student.count(0)
    return answer