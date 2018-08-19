"""
Little Shino loves maths. Today her teacher gave her two integers. Shino is now wondering how many integers can divide both the numbers. She is busy with her assignments. Help her to solve the problem.

Input:
First line of the input file contains two integers, a and b.

Output:
Print the number of common factors of a and b.
"""


a=list(map(int,input().split()))
print(len([i for i in range(1,min(a[0],a[1])+1) if (a[0]%i==a[1]%i==0)]))