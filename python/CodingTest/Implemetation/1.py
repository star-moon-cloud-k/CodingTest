#!/usr/bin/python3

#공간 N의 크기 받기
from urllib.parse import ParseResultBytes


N = int(input())

#이동 경로받기
move = list(input().upper().split())
#좌표 설정
x = 1
y = 1

#N 공간 밖으로 나가는 것은 무시함

for i in move:
    if i == 'D':
        if x == N:
            pass
        else:  x += 1
    if i == 'U':
        if x == 1:
            pass
        else : x -= 1
    if i == 'L':
        if y ==1:
            pass
        else: y -= 1
    if i == 'R':
        if y == N:
            pass
        else : y += 1
    
print(x ,',', y)    
    
         
        