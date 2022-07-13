#!/usr/bin/python3



#좌표 받기 a1 a == column 1 == row
input = input()

row = int(input[1])
column = int(ord(input[0])) - ord('a') +1       #input(0)은 'a' -> 1 ,1 으로 초기 값 설정

moves = [(-2, 1), (-2, -1), (2 , -1) , (2, 1) , (1, 2) , (1, -2), (-1, 2), (-1 , -2)]

counter = 0

for move in moves:
    x_tmp = row + move[0]
    y_tmp = column + move[1]
    
    if x_tmp < 1 or x_tmp > 8 or y_tmp > 8 or y_tmp < 1:
        continue
    counter += 1

print(counter)


