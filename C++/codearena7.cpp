/*
You are given a square matrix of size n. Rows are indexed 1 to n from top to bottom and columns are
indexed 1 to n form left to right. Matrix consists of only '*' and '.'. You need to check whether matrix is symmetric or not.
if it is, check it is symmetric about vertical axis or horizontal axis or both.

A matrix is said to be symmetric about horizontal axis if  row is identical to  row,  is identical to  row and so on...

A matrix is said to be symmetric about vertical axis if  column is identical to nth column,  identical to  and so on for
all columns.

INPUT :

First line contains t,the number of test cases. First line of each test case contains n the size of matrix.
Each of next n lines contain n characters.

OUTPUT:

Output t lines, answer for each test case. Print "HORIZONTAL" if symmetric about horizontal axis.
Print "VERTICAL" if symmetric about vertical axis. Print "BOTH" if symmetric about both axes. print "NO" if it is not symmetric.
*/

#include<iostream>
using namespace std;

int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        char chr[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>chr[i][j];
            }
        }
        bool h=true;
        bool v=true;


        for(int i=0;i<n/2;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(chr[i][j]!=chr[n-i-1][j])
                    h=false;
            }
        }
        for(int i=0;i<n/2;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(chr[j][i]!=chr[j][n-i-1])
                    v=false;
            }
        }

        if(h & v)
            cout<<"BOTH\n";
        else if(h)
            cout<<"HORIZONTAL\n";
        else if(v)
            cout<<"VERTICAL\n";
        else
            cout<<"NO\n";
    }

    return 0;
}
