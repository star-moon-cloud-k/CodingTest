#!/usr/bin/python3

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

number_of_lines = int(input())

#처음 푼 방법
# for i in range(1, number_of_lines+1):
#     for j in range(i):
#         print("*", end='')
#     print(end='\n')
    
# 두번째 푼 방법
for i in range(1, number_of_lines+1):
    print("*"*i)