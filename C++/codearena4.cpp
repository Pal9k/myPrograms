#include<iostream>
#include<string.h>

using namespace std;

// Program of Swapping of letters in string!!!
int main() {
	int num;
	// enter number of swapping need to occur
	cin >> num;
	char a[num][2];
	string str;
	// enter two letters
	// First the letter to be replace by Second letter in place of first letter!
	for(int i=0;i<num;i++)
	{
	    cin>>a[i][0];
	    cin>>a[i][1];
	}
	// enter string in which the swapping will occur !
	cin>>str;

	for(int i=0;i<str.length();i++)
	{
	    for(int j=0;j<num;j++)
	    {
	        if(str[i]==a[j][0])
	        {
	            str[i]=a[j][1];
	            break;
	        }
	        else if(str[i]==a[j][1])
	        {
	            str[i]=a[j][0];
	            break;
	        }
	    }
	}
	// print new string after swapping !!
	cout<<str;

}

