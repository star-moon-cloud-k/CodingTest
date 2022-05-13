#!/usr/bin/python3

input_list = input().split()

if input_list[0] > input_list[1]:
    print('>')
elif input_list[0] < input_list[1]:
    print('<')
else:
    print('==')
