/* C++ code to generate all possible subsequences.
	Time Complexity O(n * 2^n) */
#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n=5;
	int a[n];
	for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for (int counter = 1; counter < pow(2,n); counter++)
	{
		for (int j = 0; j < n; j++)
		{
			/* Check if jth bit in the counter is set
				If set then print jth element from arr[] */
			if (counter & (1<<j))
				cout << a[j] << " ";
		}
		cout << "\n";
	}
	return 0;
}
