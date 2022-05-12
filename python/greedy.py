def solution(n, lost, reserve):
    
    for i in lost:
        print(i)
    for i in lost:
        print(i)
        if i in reserve:
           # lost.remove(i)
            reserve.remove(i)
        elif i-1 in reserve:
            #lost.remove(i)
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            #lost.remove(i)
            reserve.remove(i+1)
            
    answer = n - len(lost)
    return answer

solution(5, [2,4] , [1,3,5])