#include<stdio.h>
#include<conio.h>
main()
{
	int n, i, j, check, A[1000], k=0, count =0;
//	printf("\n Upto How many prime no. you want to print :");
	scanf("%d", &n );
	
	// Prime No. Logic 
	for (i=2; i<=n; i++)
    {
	 check=1;     // Set flag true
	
	 for(j=2; j<=i/2; j++)
      if (i%j==0)
	    { check = 0;     // Set flag false ( Not a prime number
	       break;        // go for next number
	    }
	    
	 if (check ==1)   
	 {
	   A[k] =i;
	   k++;
//	   printf("  %d ", i);
     }
	}
	
//	printf("\n%d", k);
	
	for(i=2; i<k; i++)
	{
		int sum = 0;
		for (j = 0; j<k; j++)
		{
			sum = sum + A[j];
			if (sum == A[i])
			{
				count++;
				break;
			}
			if (sum > A[i])
			{
				break;
			 } 	
		}
	}
	printf("%d", count);
    getch();
}

