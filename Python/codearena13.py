"""
Given a number find the number of trailing zeroes in its factorial.

Input Format

A single integer - N

Output Format

Print a single integer which is the number of trailing zeroes.
"""

n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
string=(str(fact))
cnt=0
i=len(string)-1
while (i!=-1):
	if string[i]!='0':
			break
	cnt+=1
	i-=1
print(cnt)