import java.util.Scanner;
 class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i,j,n,count=0,k=0;
        // Main t = new Main();
        
        int[] a = new int[1000];
        
        // System.out.println("Enter no");
        n = sc.nextInt();
        
        for (i = 1; i <= n; i++)  	   
          { 		 		  
             int check=0; 		  
             for(j =i; j>=1; j--)
             {
    	    if(i%j==0)
    	    {
    		check = check + 1;
    	    }
    	 }
    	 if (check ==2)
    	 {
    	    a[k] =i;
    	    k++;
    	   // System.out.print(i);
    	 }	
          }	
            
        for(i=2; i<k; i++)
    	{
    		int sum = 0;
    		for (j = 0; j<k; j++)
    		{
    			sum = sum + a[j];
    			if (sum == a[i])
    			{
    				count++;
    				break;
    			}
    			if (sum > a[i])
    			{
    				break;
    			 } 	
    		}
    	}
        System.out.println(count);
    }

}