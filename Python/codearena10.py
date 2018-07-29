"""
Chandu is weak in maths. His teacher gave him homework to find maximum possible pair XOR in a matrix of size N x M with some conditions. Condition imposed is that, the pair can be formed between sum of elements in a column and sum of elements in a row. 
See sample explanation for more details.

Input:
First line consists of two integers N, M.
Next N line contains M space separated integers denoting the value of matrix entry.

Output:
For each test case output a single integer denoting the max value of XOR according to the condition.

"""

a=raw_input().split()
n=int(a[0])
m=int(a[1])
arr=[]
for x in range(0,n):
	temp=list(map(int,raw_input().split()))
	arr.append(temp)

raw=[]
for i in range(0,n):
	raw.append(sum(arr[i]))

col=[]
for i in range(0,m):
	cnt=0
	for j in range(0,n):
		cnt+=arr[j][i]
	col.append(cnt)

maxi=col[0]^raw[0]
for i in range(0,n):
	for j in range(0,m):
		if maxi<(raw[i]^col[j]):
			maxi=raw[i]^col[j]

print(maxi)
	
