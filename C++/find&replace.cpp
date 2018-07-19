#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

int main()
{
    string str;
    ofstream fptr;
    char w_find[20];
    char w_replace[20];
    fptr.open("File.txt");
    fptr<<"asgdhjkmnbsasdsfgdfhjkl\n";
    fptr<<"rtgegthyjukiokjhgfd\n";
    fptr<<"rbvecw Palak bgfwdwefg";
    fptr.close();

    cout<<"Enter word you want to find:";
    cin>>w_find;
    cout<<"enter word you want to replace:";
    cin>>w_replace;

    ifstream fin;
    fin.open("File.txt");
    while(!fin.eof())
    {
        getline(fin,str);

        char char_array[200];
        cout<<str<<"\n";
        strcpy(char_array, str.c_str());
        cout<<char_array<<"\n";

        if(strstr(char_array,w_find))
        {

            str.replace(str.find(w_find),strlen(w_find),w_replace);
            cout<<str;
        }
    }
    return 0;
}
