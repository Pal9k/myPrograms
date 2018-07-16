t=int(input())
for i in range(0,t):
    a=input()
    a=a.split()
    r=int(a[0])
    k=int(a[1])
    
    very_cool=0
    for num in range(1,r+1):
        cool=0
        binary=bin(num)
        for j in range(2,len(binary)-2):
            if binary[j]=='1':
                if binary[j+1]=='0' and binary[j+2]=='1':
                    cool+=1
        if cool>=k:
            very_cool+=1
    print(very_cool)