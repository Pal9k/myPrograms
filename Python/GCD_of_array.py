def GCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd

a=[60,48]
temp=a[0]
for num in range(1,len(a)):
	temp=GCD(temp,a[num])

print(temp)