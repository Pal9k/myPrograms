#include<iostream>
#include<fstream>
#include<ctype.h>

using namespace std;

int main()
{
	int vowels=0;
	char c;
	ofstream fout;
	fout.open("TEXT_FILE");
	fout << "abcdefghijklmnopqrstuvwxyz\n";
	fout << "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n";
    fout.close();

    ifstream fin;
    fin.open("TEXT_FILE");

	while (fin)
	{
	    fin.get(c);
	    cout<<c;
		if (tolower(c)=='a' || tolower(c)=='e' || tolower(c)=='i' || tolower(c)=='o' || tolower(c)=='u')
			vowels+=1;
	}
	cout<<"Vowels="<<vowels;
	fin.close();
	return 0;
}
