#include<iostream>
using namespace std;
int main()
{
   long int t, a[100], k=1;
   cin>>t;
   for(int j =1; j<=t; j++)
   {
   	  int n;
   	  cin>>n;
   	  int cnt=0;
   	  while(n>0)
   	  {
   	  	n = n/2;
		cnt++;   	  	
	  }
	  a[k]=cnt;
	  k++;
   }
   for (int i=1; i<k; i++)
   		printf("\n%d", a[i]);
   return 0;
}
