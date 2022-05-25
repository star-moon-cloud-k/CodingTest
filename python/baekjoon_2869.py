#!/usr/bin/python3

up , sleep , height = map(int, input().split())

go_up = 0
day = 0
for _ in range(height):
    go_up += up
    if go_up >= height:
        day += 1
        break
    
    go_up -= sleep
    day += 1

print(day) 