// one of the code from fight of codearena !!!
#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;
	int a[num];
	for(int i=0;i<num;i++)
	{
	    cin>>a[i];
	}
	for(int i=1;i<num;i++)
	{
	        for(int j=0;j<i;j++)
	        {
    	            if(a[i]<=a[j])
    	                a[j]++;
	        }
	}
	for(int i=0;i<num;i++)
	{
	    cout<<a[i]<<" ";
	}
}
