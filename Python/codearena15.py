"""
Roy is going through the dark times of his life. Recently his girl friend broke up with him and to overcome the pain of acute misery he decided to restrict himself to Eat-Sleep-Code life cycle. For N days he did nothing but eat, sleep and code.

A close friend of Roy kept an eye on him for last N days. For every single minute of the day, he kept track of Roy's actions and prepared a log file.

The log file contains exactly N lines, each line contains a string of length 1440 ( i.e. number of minutes in 24 hours of the day).
The string is made of characters E, S, and C only; representing Eat, Sleep and Code respectively. ith character of the string represents what Roy was doing during ith minute of the day.

Roy's friend is now interested in finding out the maximum of longest coding streak of the day - X.
He also wants to find the longest coding streak of N days - Y.
Coding streak means number of C's without any E or S in between.

See sample test case for clarification.

Input:
First line of each file contains N - number of days.
Following N lines contains a string of exactly 1440 length representing his activity on that day.

Output:
Print X and Y separated by a space in a single line.
"""



t=int(input())
string=[]
for z in range(0,t):
    string.append(input())
    
n=len(string)
cnt=0
cnt_arr=[]
cnt1_arr=[]
X=[]
Y=[]
cnt1=0
for i in range(0,n):
    cnt=0
    cnt_arr=[]
    cnt1_arr=[]
    for char in string[i]:
        if char=='C':
            cnt+=1
            cnt1+=1
        else:
            cnt_arr.append(cnt)
            cnt1_arr.append(cnt1)
            cnt=0
            cnt1=0
    X.append(max(cnt_arr))
    Y.append(max(cnt1_arr))
    
print("{} {}".format(max(X),max(Y)))