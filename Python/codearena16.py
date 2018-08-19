"""
Ashu is very fond of Prime numbers and he like challenging his friends by giving them various problems based on Mathematics and Prime number. One of his friend Harshit is jealous and challenges him to solve a task. Task is :
Given a prime number X, you need to give the count of all numbers in range 1 to 106 inclusive which have minimum prime factor X.
Help Ashu in solving this task.

Input:
First line consist of numer of test cases T.
Each test case contains a single number X.

Output:
Output for each test case count of all numbers in range 1 to 106 inclusive which have minimum prime factor X.
"""


def isPrime(n):
     
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True
 



t=int(input())
for z in range(0,t):
    n=int(input())
    cnt=0
    for num in range(1,10**6+1):
        flag=True
        for i in range(2,n):
            if num%i==0:
                if isPrime(i):
                    flag=False
        if flag:
            if num%n==0:
                cnt+=1
    print(cnt)