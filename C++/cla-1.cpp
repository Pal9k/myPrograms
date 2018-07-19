// the program for command line argument to copy content of one file into another file

#include<iostream>
#include<fstream>
using namespace std;

int main(int argc, char **argv)
{
    fstream source,desti;
    source.open(argv[1],ios::in);
    desti.open(argv[2],ios::out);
    char ch;
    while(!source.eof())
    {
        source.get(ch);
        desti.put(ch);
    }
    source.close();
    desti.close();

    return 0;
}

// command need to enter in command line
// for compile program
//      g++ .\cla-1.cpp -o main
// for run program
//      .\cla-1.exe File1.txt File2.txt
// file1.txt is the source file file2 .txt is destination file
// note: both file need to be created within same location of program
