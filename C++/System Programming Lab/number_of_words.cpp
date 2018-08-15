#include<iostream>
#include<fstream>
#include<ctype.h>

using namespace std;

int main()
{
	int cnt=0;
	char c;

    ifstream fin;
    fin.open("hi.txt");

	while (fin)
	{
	    fin.get(c);
	    cout<<c;
		if(c==' ' || c=='\n' || c=='\t')
			cnt++;

	}
	cout<<"\nWords="<<cnt;
	fin.close();
	return 0;
}


