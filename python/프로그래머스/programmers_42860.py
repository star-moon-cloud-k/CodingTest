#!/usr/bin/python3
def solution(name):
    answer = 0
    str_list = [chr(i) for i in range(65 , 91)]
    joystick_up_down = []

    mid = (65+90)/2
    print(str_list)
    #mid_less = X - 65
    #mid_more = 90 - X
    
    for i in range(len(name)):
        char = ord(name[i])
        print(i)
        if char > mid :
            joystick_up_down.append(90 - char)
        elif char < mid :
            joystick_up_down.append(char - 65)
        
    sum_list = sum(joystick_up_down)
        
            
        
    return sum

def main():
    solution(input())

if __name__ == "__main__":
    main()