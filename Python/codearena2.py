n=int(input())
for num in range(0,n,1):
    string=raw_input()
    l=len(string)
    temp=[]
    for char in string:
        temp.append(ord(char))

    temp.sort(reverse=True)
    char=[None for i in range(0,l)]

    mid=int(l/2)
    cnt=0
    for n in range(0,l):
        if char[mid+cnt]==None:
            char[mid+cnt]=temp[n]
        else:
            char[mid-cnt]=temp[n]

        if n%2==0:
            cnt+=1
         
    for i in range(0,len(string)):
        char[i]=chr(char[i])
    print(''.join(char))
        


