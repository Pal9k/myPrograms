# the problem in which n number of people are standing side by side each other in circle
# the the sword is in first no. of people having 
# which will kill people next to him n give sword to third people standing in the circle
# the third people will kill people standing next to him n give sword to next of next people
# n this process carry on util there will be one people in the circle
# the input will be number of people n output will be the last number of  people do alive!
n=100

old=[i+1 for i in range(0,n)]

print old

#first need to alive
first = True

while(len(old)!=1):
	new=[]
	# first need to alive so even numbers of elements keep alive!
	if first:
		for i in range(0,len(old)):
			if i%2==0:
				new.append(old[i])
	# first need to die so odd numbers of elements keep alive!
	else:
		for i in range(0,len(old)):
			if i%2!=0:
				new.append(old[i])
	print new
	# check if sword is in last member or not!
	# from that decide first need to alive or die!
	if old[-1]==new[-1]:
		first = False
	else:
		first=True
	# make old array referenceing to new array!
	old=new