#include <stdio.h> 
int main()
	{
	int samples[1000], result[100],s,i,j,t,l1,l2,c=0, cnt =0;
	scanf("%d",&s);
	scanf("%d",&t);
	
	for(i=0;i<s;i++)
	scanf("%d",&samples[i]);
	
	for(i=0;i<t;i++)
	{
		scanf("%d %d",&l1,&l2);
		for(j=0;j<s;j++)
		{
		  if((samples[j]>=l1)&&(samples[j]<=l2))
		  c++;
		}
		result[cnt++] = c;
//		printf("%d ",c);
		c=0;
	}
	for(i=0; i<t; i++)
		printf("%d ", result[i]);
	return 0;
}
