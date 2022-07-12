
Number, Divide = map(int, input().split())

counter = 0

while Number >= Divide:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while Number % Divide != 0:
        Number -= 1
        counter += 1
    
    #K로 나누기
    Number //= Divide
    counter += 1
    
#마지막으로 남은 수에 대하여 1씩 빼기
while Number > 1:
    Number -= 1
    counter += 1
    

print(counter)


            
        


