#!/usr/bin/python3

m , n = map(int, input().split())       #행열 크기 설정

mini = 0
for i in range(m):
    array_rows = list(map(int, input().split()))   #row 설정
    minimum = min(array_rows)
    if mini < minimum:
        mini = minimum
    
print(mini)
    
