"""
Raj stays at a hostel. He has N friends, numbered from 1 to N.

One day, when he woke up at time p:q, he found his slippers to be missing.
He couldn't go out to get a new slipper on bare foot. So, he wants to borrow slippers from one of his friends to go to the store to get a new slipper. But there are 5 conditions he must follow:

The hostel has an in-time of x:y . He has to return back before x:y.

The footwear store in that area opens at a time a:b, only after which a slipper can be selected and bought, no matter how early Raj goes to the shop. Once the shop is opened, it stays open throughout the day.

He can borrow the slippers from his friend numbered x, only if x does not use his slippers in the time interval that Raj asks for. 
Luckily, all of Raj's friends are lazy and hence they use their slippers exactly once a day. For each friend, you are given h1:m1 and h2:m2. The friend uses his slippers from h1:m1 to h2:m2 (inclusive)

if Raj has the option to use the slippers of friend i and friend j such that i<j, he would prefer to use the slipper of friend i.

It takes Raj R minutes to travel from the store to his hostel and from his hostel to the store, both . Once he is at the store, it takes him S minutes to select a new slipper.

Raj wants to go to the footwear store, select and buy a new slipper and return to the hostel at the earliest. Given all the required information, find the friend from whom Raj should borrow the slippers.
He can start his journey after he wakes up, that is, after p:q

Input:
First line contains an integer T, denoting the number of test cases to follow.

Each testcase begins with an integer N. The next 5 lines contains:
1. The in-time of the hostel, x:y,
2. Time at which Raj wakes up, p:q
3. The time from which the Footwear store will be open, a:b
4. Integer R denoting the minutes it takes to travel between the store and his hostel 
5. Integer S denoting the minutes Raj takes to select a new slipper.

N lines follow. The ith line contains the time interval during which his ith friend use his slippers in the format "h1:m1 h2:m2"

Hence, each testcase contains N+6 line.

(Strictly follow the format given in the sample Testcase for input and output)

Output: 
If it is possible to get slippers on that day, print the index of the friend from whom Raj should borrow the slippers, adhering to the above mentioned conditions.
Else print "-1" to denote that he cannot get the slippers before the day end.

Constraints
0<=T<=100
0<=N<=200
0<=R,S<(24*60)
h1:m1 <= h2:m2
All the times are given as hours:minutes. (0<=hours<=23, 0<=minutes<=59) ( See 24 - hour format )
Note: hours and minutes will always be a two digit integer, Eg: 09:05, 13:09

Sample Case:
1
5
21:30
06:00
09:00
25
10
07:00 10:00
08:30 09:20
12:00 13:45
06:00 16:00
12:05 15:00

Sample Output:
3
"""


def less_than(a,b):
	if a[0]<b[0]:
		return True
	elif a[0]>b[0]:
		return False
	else:
		if a[1]<b[1]:
			return True
		else:
			return False


def equal(a,b):
	if a[0]==b[0]:
		if a[1]==b[1]:
			return True
	return False	

# take all inputs
t=int(input())
for z in range(0,t):
	n=int(input())
	x_y=list(map(int,raw_input().split(":")))
	p_q=list(map(int,raw_input().split(":")))
	a_b=list(map(int,raw_input().split(":")))
	r=int(input())
	s=int(input())
	time_buddy=[]
	for i in range(0,n):
		temp=raw_input().split()
		temp[0]=list(map(int,temp[0].split(":")))
		temp[1]=list(map(int,temp[1].split(":")))
		time_buddy.append(temp)


	final_time=[0,0]			# final time is hr n min to go shop n to return 
	if less_than(p_q,a_b):			# person wakes up early before shop opens
		temp=r+s
	else:							# person wakes up late after opening shop
		temp=2*r+s

	temp=[temp/60,temp%60]			# calculate final time needed coming back hostel assuming he have slippers
	final_time[1]=a_b[1]+temp[1]
	final_time[0]=a_b[0]+temp[0]
	final_time[0]+=final_time[1]/60
	final_time[1]=final_time[1]%60


	time=[]							# time[1] will have time when person can back to hostel using 1st friend slippers
	for i in range(0,n):
		if less_than(time_buddy[i][0],final_time) or equal(time_buddy[i][0],final_time):
			temp1=[0,0]
			temp1[1]=time_buddy[i][1][1]+(2*r+s)
			temp1[0]=time_buddy[i][1][0]
			temp1[0]+=temp1[1]/60
			temp1[1]=temp1[1]%60
			time.append(temp1)
		else:
			time.append(final_time)


	mini=time[0]					# minimon time person need to come back to hostel buying new slippers
	index=0
	for i in range(0,n):
		if less_than(time[i],mini):
			mini[0]=time[i][0]
			mini[1]=time[i][1]
			index=i

									# checks if minimon time less than hostel`s limiting time?
	if less_than(mini,x_y) or equal(mini,x_y):
		print(index+1)
	else:
		print("-1")
