#N까지의 시간 입력

n = int(input())

Hours = 0
Minutes = 0
Seconds = 0

counter = 0
for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second)  :
                counter += 1

print(counter)            