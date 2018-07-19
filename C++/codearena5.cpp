/*Little Arjit is in love with Deepa. They have always thought of themselves as the ideal couple - the best, possible match they could've managed. (No kidding!) And like every other couple, they promised each other not to fight after every other fight. But, when has that happened before?

But, this is a different couple - this is a programming couple - and they argue on weird things, like Fibonacci numbers, prime numbers, Sterling numbers, and what not!

Their recent fight might seem silly to a lot of people, but it is a matter of serious concern for both of them. They have bought a cake, and they weighed it in milligrams - the weight of the cake is always even and now they wish to divide the cake between them in some way, that both of them are satisfied.

Arjit challenges Deepa that if she can divide the weight of the cake as sum of two prime numbers between them, she can have the entire cake - and if she fails to do so, he'll get the cake.

The argument is getting more, and more heated now - please help them sort out their stupid arguments or an easier way would be to help them figure out who is going to have the cake.

Input Format:
The first line will contain a number, tc, denoting the number of test cases.

The next tc lines will contain an even number, denoting the weight of the cake in milligrams.

Output Format:
Print "Arjit" or "Deepa" according to the winner.
*/

#include<iostream>
using namespace std;

bool prime(int);

int main()
{
    int tc,n;
    bool flag=false;
    cin>>tc;
    while(tc--)
    {
        cin>>n;
        int num1=2;
        while(num1<n)
        {
            if(prime(num1))
            {
                int num2=n-num1;
                if(prime(num2))
                {
                    flag=true;
                    cout<<"num1="<<num1<<" num2="<<num2<<"\n";
                    cout<<"Deepa\n";
                    break;
                }
            }
            num1++;
        }
        if(!flag)
            cout<<"Arijit\n";
    }
    return 0;
}

bool prime(int num)
{
    for(int i=2;i<num;i++)
    {
        if(num%i==0)
            return false;
    }
    return true;
}
