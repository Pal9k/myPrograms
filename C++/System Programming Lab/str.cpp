#include<iostream>
using namespace std;

int main()
{
    string str;
    cin>>str;
    for(int i=0;i<=sizeof(str);i++)
    {
        cout<<" "<<str[i];
    }


    return 0;
}
