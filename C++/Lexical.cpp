#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

char spchar[]={',',';','(',')','{','}','[',']','#'};
char oper[]={'+','-','*','/','%','=','!','<','>'};
string key[]={"int","float","char","double","bool","void","extern","unsigned","goto","static","class","struct","for","if","else","return","register","long","while","do","include","define","main"};
string header[]={"stdio.h","conio.h","malloc.h","process.h","string.h","ctype.h"};

bool check_oper(char);
bool check_spchar(char);
bool check_key(string);
bool check_header(string);
void bucket(string);

int main()
{
    char c;
    ifstream fin;
    fin.open("demo.cpp");
    char array_token[200][254];
    int chr=0;
    int line=0;
    bool pre_char=false;
	while (fin)
	{
	    fin.get(c);
	    if(c==' ')
        {
            bucket(array_token[line]);
            line++;
            chr=0;
            continue;
        }
        else if(c=='\n')
        {
            if(chr!=0)
            {
                bucket(array_token[line]);
                line++;
                chr=0;
            }
        }
        else if(c=='\t')
        {
            continue;
        }
        else if(check_spchar(c))
        {
            if(!pre_char)
            {
                pre_char=false;
                bucket(array_token[line]);
                line++;
                chr=0;
            }
            cout<<"Special character = "<<c<<"\n";
            array_token[line][chr]=c;
            pre_char=true;
            line++;
            chr=0;
        }
        else if(check_oper(c))
        {
            if(!pre_char)
            {
                bucket(array_token[line]);
                pre_char=false;
                line++;
                chr=0;
            }
            cout<<"Operator = "<<c<<"\n";
            array_token[line][chr]=c;
            pre_char=true;
            line++;
            chr=0;
        }
	    else
        {
            array_token[line][chr++]=c;
            pre_char=false;
        }

	}

    for(int k=0;k<50;k++)
    {
        cout<<array_token[k]<<"\n";
    }
    return 0;
}

bool check_spchar(char c)
{
    for(int i=0;i<10;i++)
    {
        if(c==spchar[i])
        {
            return true;
        }
    }
    return false;
}

bool check_oper(char c)
{
    for(int i=0;i<10;i++)
    {
        if(c==oper[i])
        {
            return true;
        }
    }
    return false;
}

bool check_key(string str)
{
    for(int i=0;i<23;i++)
    {
        if(str==key[i])
            return true;
    }
    return false;
}

bool check_header(string str)
{
    for(int i=0;i<6;i++)
    {
        if(str==header[i])
            return true;
    }
    return false;
}

void bucket(string str)
{
    if(check_key(str))
        cout<<"key = "<<str<<"\n";
    else if(check_header(str))
        cout<<"Header file = "<<str<<"\n";
    else
        cout<<"Identifier = "<<str<<"\n";
}

