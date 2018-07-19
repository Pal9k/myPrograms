/*
Oz has a list arr[] of M integers. He has to find all integers K such that :

1) K > 1
2) arr[1]%K = arr[2]%K = arr[3]%K = ... = arr[M]%K where '%' is a modulus operator
Help Oz to find all such K's.

Input :
First line of input contains an integer M. Then M lines follow each containing one integer of the list.
Input data is such that at least one integer K will always exist.

Output :
Output all possible integers K separated by space in increasing order.
*/

#include<iostream>
using namespace std;

int main()
{
    int m;
    cin>>m;
    int a[m];
    for(int i=0;i<m;i++)
    {
        cin>>a[i];
    }
    bool flag;
    for(int i=2;i<10;i++)
    {
        flag=true;
        int reminder=a[0]%i;
        for(int j=0;j<m;j++)
        {
            if(a[j]%i!=reminder)
                flag=false;
        }
        if(flag==true)
            cout<<i<<" ";
    }

    return 0;
}
