"""
In a village far far away, lived a farmer named Zico. He was finding it difficult to make his two ends meet and hence, approached the god of grains, Azure. Azure granted him a blessing:

"I shall grant thou P units of food initially . After every year, thou shall come to me and the food units shall increase by a value M i.e P+M, P+M+M, ... and so on. But remember, every year the population of your village shall multiply by a factor of '2' and you must divide the food evenly among all villagers."

Zico returns back , calculates how many total units of food will he be able to secure for himself, if he becomes immortal and keeps going to Azure till the end of time and space, as we know it.

Note: 
-Assume Zico is the only one in the village i.e Initial Population=1

INPUT
First line contains an integer T. T testcases follow. 
Each test case contains two space-separated integers P, M 

OUTPUT
For each test case, output the answer in a new line. 
"""

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