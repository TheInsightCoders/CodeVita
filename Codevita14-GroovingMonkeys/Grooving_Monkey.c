#include<stdio.h>
long long int gcd(long long int a,long long int b)
{
  if(b==0)
    return a;
  else
    return gcd(b,a%b);
}
int main()
{
  long long int t,n,i,res,c,temp,temp1;
  scanf("%lld",&t);
  while(t--)
  {
    scanf("%lld",&n);
    long long int a[n];
    for(i=0;i<n;i++)
      scanf("%lld",&a[i]);
    i=0;
    res=1;
    c=0;
    while(i<=n-1)
    {
      temp1=i;
      c=0;
      while(a[i]!=0)
      {
        temp=i;//4
        i=a[i]-1;//0
        a[temp]=0;//0
        c+=1;//3
      }
      i=temp1+1;
      if(c!=0)
        res=res*c/gcd(res,c);
    }
    printf("%lld\n",res);
  }
  return 0;
}
