"""
Xenny was a teacher and his class consisted of N boys and N girls. He took all his students to the playground and asked them to stand in a straight line. The boys and the girls formed a perfect line, but Xenny seemed unhappy. He wanted them to form an alternating sequence of boys and girls, i.e., he wanted that after a boy, there should be a girl in the line, and vice-versa.

In order to form an alternating sequence, a boy and a girl could swap their positions.

Given the original sequence in which the boys and girls were standing, find the minimum number of swaps required to form an alternating sequence.

Note: An alternating sequence can start either with a boy or a girl.

Input
First line of input consists of a natural number T - the number of testcases.
T testcases follow. For each testcase:

First line consists of a single integer N - the number of boys, and the number of girls.
Second line consists of a string of length , representing the original sequence.
In this string, a boy is represented by uppercase character B and a girl by G.

Output
For each testcase, print the minimum number of swaps required to get an alternating sequence on a new line.
"""

t=int(input())
for z in range(0,t):
	n=int(input())
	string=str(input())
	cnt1=0
	cnt2=0
	for i in range(0,len(string)):
		if i%2==0:
			if string[i]!='G':
				cnt1+=1
		else:
			if string[i]!='B':
				cnt1+=1

	for i in range(0,len(string)):
		if i%2==0:
			if string[i]!='B':
				cnt2+=1
		else:
			if string[i]!='G':
				cnt2+=1
	cnt1/=2
	cnt2/=2
	
	if cnt1<cnt2:
		print(int(cnt1))
	else:
		print(int(cnt2))
