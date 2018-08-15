#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

void func(string a1,string a2,string a3,int col,bool empt);

int main()
{
    string str;
    ifstream fin;
    fin.open("assembly.txt");
    char arr[200][3][30];
    int line=0,chr=0;
    int col=0;
    bool empt;
    while(getline(fin,str))
    {
        getline(fin,str);
        cout<<str;
        for(int i=0;i<=sizeof(str);i++)
        {
            if(str[i]=='\t')
            {
                col+=1;
                if(chr==0)
                    empt=false;
                else
                    empt=true;
                //func(arr[line],col,empt);
                chr=0;
                line++;
            }
            else
                arr[line][col][chr++]=str[i];

        }
        if(chr==0)
            empt=false;
        else
            empt=true;
        func(arr[line][0],arr[line][1],arr[line][2],col,empt);
        line++;
        chr=0;
        col=0;

    }


    return 0;
}
void func(string a1,string a2,string a3,int col,bool empt)
{
    /*
    if(empt)
    {
            if(strcmp(a,"START")==0)
                cout<<"heyy";
    }*/

    //cout<<"1."<<a1<<"   2."<<a2<<"3."<<a3<<"\n";

    //cout<<a<<" ";
    //cout<<col<<"\n";
}

