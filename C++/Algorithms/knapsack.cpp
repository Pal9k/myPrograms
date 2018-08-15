#include<iostream>
using namespace std;

int main()
{
    int n=5;
    int v[]={20,30,66,40,60};
    int w[]={10,20,30,40,50};
    double v_w[n];
    int max_weight=100;

    for(int i=0;i<n;i++)
    {
        v_w[i]=double(v[i])/w[i];
    }

    double temp;
    int temp1;
    for(int i=0;i<n-1;i++)
    {
       for(int j=0;j<n-1;j++)
       {
           if (v_w[j]<v_w[j+1])
           {
               temp=v_w[j];
               v_w[j]=v_w[j+1];
               v_w[j+1]=temp;

               temp1=v[j];
               v[j]=v[j+1];
               v[j+1]=temp1;

               temp1=w[j];
               w[j]=w[j+1];
               w[j+1]=temp1;
           }
       }
    }


    int i=0;
    double value=0;
    while(true)
    {
        if(w[i]<max_weight)
        {
            max_weight-=w[i];
            value+=v[i];
            //cout<<"max_weight="<<max_weight<<"value="<<value<<"\n";
            i++;
        }
        else
        {
            double temp=(float)max_weight/w[i];
            value+=temp*v[i];
            //cout<<"max_weight=0"<<"value="<<value<<"\n";
            break;
        }
    }
    cout<<"value="<<value;


    return 0;
}
