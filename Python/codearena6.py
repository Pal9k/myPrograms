t=int(input())
for z in range(0,t):
	a=raw_input()
	a=a.split()
	p=int(a[0])
	m=int(a[1])
	population=2
	food=p+m
	total_food=p
	while(True):
		my_food=float(food)/population
		if(round(my_food,20)==0):
			print(total_food)
			break
		total_food=total_food+my_food
		food+=m
		population*=2