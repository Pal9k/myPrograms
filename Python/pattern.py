
def process(n,ch):
    cnt=n+1
    cnt1=4
    for i in range(1,n+1,1):
        if i<=(n/2)+1:
            for j in range(i,1,-1):
                print " ",
            for k in range(cnt,1,-1):
                print ch,
            cnt=cnt-2
        else:
            for j in range(n-i,0,-1):
                print " ",
            for k in range(cnt1,1,-1):
                print ch,
            cnt1=cnt1+2
        print


print process(25,'@')
