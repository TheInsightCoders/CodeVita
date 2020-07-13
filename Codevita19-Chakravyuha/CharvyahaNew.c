#include<stdio.h>
int isDivby11(int);

int main(){

    int n;
    scanf("%d",&n);

    //check contraint
    if(n<=0 || n>100){
        return 0;
    }

    int a[100][100]; // matrix to store number
    int b[20][20];   // Matrix for power point
    int counter=1;  // store the number in rectangular spiral

    int i,j,x = 1; //incices of arrays

    int w;   // w - window 

    int size=n-1; // size - size of window
    
    int no_div = (n*n)/11 + 1 ; // no of divisibles by 11

    for( w = 0 ; w < n / 2 ; w++){
        i = w;
        j = w;

        //move right
        for( j = j ; j < size + w ; j++){
        	        
            a[ i ][ j ] = counter;
            counter++;
            
            if(isDivby11( a[i][j] )){
                b[x][0]=i;
                b[x][1]=j;
                x++;
            }
        }

        //move down
        for( i = i ; i < size + w ; i++){
        				        	
            a[ i ][ j ] = counter;
            counter++;
            
            if(isDivby11( a[i][j] )){
                b[x][0]=i;
                b[x][1]=j;
                x++;
            }
        }

        //move left
        for( j = j ; j > w ; j--){
            a[ i ][ j ] = counter;
            counter++;
            
            if(isDivby11( a[i][j] )){
                b[x][0]=i;
                b[x][1]=j;
                x++;
            }
        }

        //move up
        for( i = i ; i > w ; i--){
        	          
            a[ i ][ j ] = counter;
            counter++;
            
            	if(isDivby11( a[i][j] )){
                b[x][0]=i;
                b[x][1]=j;
                x++;
            }
        }
        size = size-2;
    }
    
    // if value of n is odd
    if( n % 2 != 0){
        a[w][w] = counter;      
    }

    //print number in rectangular spiral (Chakarvyuha)
    for( i = 0 ; i < n ; i++){
        for( j = 0 ; j < n ; j++){
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }
    
    printf("Total Power points : %d\n",no_div);

    printf("(0,0)\n");
    int k;
    for (k=1; k<x; k++)
	{
		printf("(%d,%d)\n", b[k][0], b[k][1]);
	 } 
    return 0;
}

int isDivby11(int z){
    if( z % 11 == 0 ){
        return 1;
    }
    else{
        return 0;
    }
}
