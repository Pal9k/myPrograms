"""
Chef has recently been playing a lot of chess in preparation for the ICCT (International Chef Chess Tournament).

Since putting in long hours is not an easy task, Chef's mind wanders elsewhere. He starts counting the number of squares with odd side length on his chessboard..

However, Chef is not satisfied. He wants to know the number of squares of odd side length on a generic N∗N chessboard.
"""


t=int(input())
for z in range(0,t):
	n=int(input())
	cnt=0
	cnt1=0
	for i in range(1,n+1):
		if i%2!=0:
			cnt+=(i**2)
		else:
			cnt1+=(i**2)
	if cnt>cnt1:
		print(cnt)
	else:
		print(cnt1)