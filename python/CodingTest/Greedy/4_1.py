#!/usr/bin/python3

#N, K를 공백으로 구분하여 입력받기

from unittest import result


n , k = map(int , input().split())

result =0 

while True:
    #(n==k로 나누어 떨어지는 수) 가 될 때 까지 1 씩 빼기
    
    target = (n//k) * k
    result += (n-target)
    
    n  = target
    
    #n 이 k보다 작을 떄 (더 이상 나눌 수 없을 때) 반복문 탈출
    
    if n < k:
        break
    
    #k로 나누기
    result += 1
    n //= k
    
#마지막으로 남은 수에 대해 1씩 빼기
result += (n -1)
print(result)
