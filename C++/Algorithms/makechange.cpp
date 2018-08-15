#include<iostream>
using namespace std;

int main()
{
    int amount=59;
    int a[5]={100,25,20,5,1};
    int len=5;

    int i=0,s=0,q,r;
    while(amount>0)
    {
        q=amount/a[i];
        r=amount%a[i];
        amount=r;
        s=s+q;
        i++;
    }
    cout<<"The number the coins are "<<s;


    return 0;
}
