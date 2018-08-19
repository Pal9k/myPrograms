"""
Assume there is an Ideal Random Number Generator which generates any real number between 0 and given integer. Two numbers are generated from the above generator using integer A and B, let's assume the numbers generated are X1 and X2. There is another integer C. What is the probability that summation of X1 and X2 is less than C.

Input Format
A single line containing three integers A,B,C
1 <= A,B,C <= 100000

Output Format
Print the probability in form of P/Q
"""


a=list(map(int,input().split()))
if a[0]+a[1]>a[2]:
    print("1/2")
else:
    print("1")