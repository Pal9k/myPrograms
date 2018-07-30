#Program to find cartesian product of any number of sets


# function to find cartesian for two sets 
def cartesianProduct(set_a , set_b):
	result=[]
	for i in range(0,len(set_a)):
		for j in range(0,len(set_b)):
			# for handling case having cartesian prodct first time of two sets
			if type(set_a[i]) != list:			
				set_a[i] = [set_a[i]]
			# coping all the members of set_a to temp
			temp = [num for num in set_a[i]]
			# add member of set_b to temp to have cartesian product		
			temp.append(set_b[j])				
			result.append(temp)				
	return result



# take input of sets
arr = []
n=int(input("Enter number of sets:"))
for cnt in range(0,n):
	temp = raw_input("Enter {} set:".format(cnt+1)).split()
	arr.append(temp)



# result of cartesian product of all the sets taken two at a time
temp = arr[0]
for i in range(1,n):
	temp = cartesianProduct(temp , arr[i])
print(temp)