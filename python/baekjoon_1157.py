#!/usr/bin/python3
from collections import Counter


input_counter = Counter(input().upper())
mc_results = input_counter.most_common(2)
print(mc_results)

if mc_results[0][1] != mc_results[1][1]:
    print(mc_results[0][0].upper())
else:
    print("?")

#for k , v in sorted(input_str.items(), key= lambda x:x[1], reverse=True):  
 #   print(k, v)
