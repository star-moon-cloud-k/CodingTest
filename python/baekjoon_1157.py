#!/usr/bin/python3
from collections import Counter

input_counter = Counter(input().upper())
mc_results = input_counter.most_common(2)

if mc_results[0][1] != mc_results[1][1]:
    print(mc_results[0][0].upper())
else:
    print("?")
