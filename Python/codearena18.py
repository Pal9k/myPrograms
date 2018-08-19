"""
Given an array A of N integers, classify it as being Good Bad or Average. It is called Good, if it contains exactly X distinct integers, Bad if it contains less than X distinct integers and Average if it contains more than X distinct integers.

Input format:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of two space separated integers denoting N and X.
Second line of each test case consists of N space separated integers denoting the array elements.

Output format:
Print the required answer for each test case on a new line.
"""


t=int(input())
for z in range(0,t):
    a=list(map(int,input().split()))
    n=a[0]
    x=a[1]
    a=list(map(int,input().split()))
    temp=[]
    for i in range(0,n):
        if a[i] not in temp:
            temp.append(a[i])
    if len(temp)==x:
        print("Good")
    elif len(temp)>x:
        print("Average")
    else:
        print("Bad")