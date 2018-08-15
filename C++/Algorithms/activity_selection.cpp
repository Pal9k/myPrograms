#include<iostream>
using namespace std;

int main()
{
    int n=8;
    int start_time[8]={1,0,1,4,2,5,3,4};
    int finish_time[8]={3,4,2,6,9,8,5,5};

    for(int i=0;i<n-1;i++)
    {
       for(int j=0;j<n-1;j++)
       {
           if (finish_time[j]>finish_time[j+1])
           {
               int temp1=finish_time[j];
               finish_time[j]=finish_time[j+1];
               finish_time[j+1]=temp1;

               int temp2=start_time[j];
               start_time[j]=start_time[j+1];
               start_time[j+1]=temp2;
           }
       }
    }

    int i=0;
    cout<<"start_time="<<start_time[i];
    cout<<"          finish_time="<<finish_time[i]<<"\n";
    int last=finish_time[i];
    while(i<n)
    {
        if(last<=start_time[i])
        {
            cout<<"start_time="<<start_time[i];
            cout<<"          finish_time="<<finish_time[i]<<"\n";
            last=finish_time[i];
        }
        i++;
    }


    return 0;
}
