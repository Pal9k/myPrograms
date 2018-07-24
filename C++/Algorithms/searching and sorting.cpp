#include<iostream>

using namespace std;

const int length=5;

int find_max(int a[]);
int find_min(int a[],int maxi);

class Array
{   public:
    int a[length];

    void get_array();
    void print_array();
};

class Searching:public Array
{
    public:
    int num;

    int linear();
    int binary();

};

class Sorting:public Array
{
    public:
    void bubble();
    void insertion();
    void selection();
    void counting();
};

void Array::get_array()
{
    cout<<"Enter array:";
    for(int i=0;i<length;i++)
    {
        cout<<"a["<<i<<"] :";
        cin>>a[i];
    }
}

void Array::print_array()
{
    for(int i=0;i<length;i++)
    {
        cout<<"a["<<i<<"] = "<<a[i]<<"\n";
    }
}

int Searching::linear()
{
    cout<<"Linear search:\n";
    cout<<"Enter num to search:";
    cin>>num;
    for(int i=0;i<length;i++)
    {
        if (a[i]==num)
        {
            return (i);
        }
    }
    return -1;
}

int Searching::binary()
{
    cout<<"Binary search\n";
    cout<<"Enter num to search:";
    cin>>num;

    int lower=0;
    int higher=length;

    while(true)
    {
        if ((lower>higher) || (lower==length-1) || (higher==0))
            return -1;

        int mid=(lower+higher)/2;
        if (a[mid]==num)
            return mid;
        else
        {
            if (num>a[mid])
            {
                lower=mid;
            }
            else
            {
                higher=mid;
            }
        }
    }
}

void Sorting::bubble()
{
    int temp;
   for(int i=0;i<length-1;i++)
   {
       for(int j=0;j<length-1;j++)
       {
           if (a[j]>a[j+1])
           {
               temp=a[j];
               a[j]=a[j+1];
               a[j+1]=temp;
           }
       }
   }

}


void Sorting::insertion()
{
    int key,j;
    for(int i=1;i<length;i++)
    {
        key=a[i];
        j=i-1;
        while(j>=0 &&a[j]>key)
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=key;
    }
}

void Sorting::selection()
{
    for(int i=0;i<length;i++)
    {
        int min_var=i;
        for(int j=i+1;j<length;j++)
        {
            if(a[j]<a[min_var])
                min_var=j;
        }
        int temp=a[i];
        a[i]=a[min_var];
        a[min_var]=temp;
    }
}

void Sorting::counting()
{
    int maxi=find_max(a);
    int mini=find_min(a,maxi);
    int r=maxi-mini+1;
    int range[r];
    for(int i=0;i<r;i++)
    {
        range[i]=mini++;
    }
    int Count[r];
    for(int i=0;i<r;i++)
    {
        Count[i]=0;
    }
    for(int i=0;i<length;i++)
    {
        for(int j=0;j<r;j++)
        {
            if(a[i]==range[j])
                Count[j]++;
        }
    }
    int cnt=0;
    for(int i=0;i<r;i++)
    {
        while(Count[i]!=0)
        {
            a[cnt++]=range[i];
            Count[i]--;
        }

    }
}

int find_max(int a[])
{
    int maxi=0;
    for(int i=0;i<length;i++)
    {
        if(a[i]>maxi)
        {
            maxi=a[i];
        }
    }
    return maxi;
}

int find_min(int a[],int maxi)
{
    int mini=maxi;
    for(int i=0;i<length;i++)
    {
        if(a[i]<mini)
            mini=a[i];
    }
    return mini;
}

int main()
{
    int index;

 /*   Searching s1;
    s1.get_array();
    index=s1.linear();
    if (index==-1)
        cout<<"Item not found!\n";
    else
        cout<<"Index is "<<index<<"\n";

    index=s1.binary();
    if (index==-1)
        cout<<"Item not found!\n";
    else
        cout<<"Index is "<<index<<"\n";
*/
    Sorting s2;
    s2.get_array();
    s2.counting();
    s2.print_array();

    return 0;
}
