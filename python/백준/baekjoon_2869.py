#!/usr/bin/python3
import math
up , sleep , height = map(int, input().split())


# day = int(height // (up - sleep))
# go_up = day - up + sleep
# if (up) >= day :
#     day += 1

# else:
#     day -= up
#     for _ in range(height):
#         go_up += up
#         if go_up >= height:
#             day += 1
#             break
#         go_up -= sleep
#         day += 1

day = (height - sleep) / (up - sleep)

print(math.ceil(day)) 