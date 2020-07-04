#include <stdio.h>
#include<math.h>
int main() 
{
	int t,n,b,i,yrs,a=0;
	double p,slab,sum,emi,bank[2],power;
	
	scanf("%lf",&p);  // p principal (Loan Amount)
	scanf("%d",&t);  // t Total Tenure (in years)
	for(b=0;b<2;b++)
	{
		scanf("%d",&n);  // No. of slabs
		sum=0;
		for(i=0;i<n;i++)
		{
		  scanf("%d",&yrs);
		  scanf("%lf",&slab);
		  power=pow((1+slab),yrs*12);
		  emi= (p*(slab))/(1-1/power);
		  sum= sum + emi;
		}
		bank[a++]=sum;	
	}
	
	if(bank[0]<bank[1])
		printf("Bank A");
	else
		printf("Bank B");
	return 0;
}
