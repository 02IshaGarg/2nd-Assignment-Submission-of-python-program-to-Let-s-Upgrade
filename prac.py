# -*- coding: utf-8 -*-
"""
Created on Fri Jan 6 20:55:36 2023

@author: Lefty Ishu
"""

# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)


def sum_list(li):
    sum = 0
    for i in li:
        sum += i
    return sum
    
sampleList = list((8, 2, 3, 0, 7))
print(sum_list(sampleList))