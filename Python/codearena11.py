"""
Little chandu is very fond of playing games. Recently, He found a few straws each of length 1 inches in the store room. He took all of them and decided to mark a rectangular area on the floor with straws and warn rest of the family members to not to enter that area so that he can play in peace. He wants to maximize that area. But, unable to do so, He seeks for your help. You being the elder brother of chandu, write a program for him to find maximum area that he can cover in inches using N straws.

Input:

First line of input contains an integer t. then, t lines follow each containing a single integer N - No of straws.

Output:

Print the area of largest rectangle that can be formed using the given sticks.
"""

import math
t=int(input())
for z in range(0,t):
    n=int(input())
    y=int(n/4)
    x=int((n/2)-y)
    area=x*y
    print(math.floor(area))