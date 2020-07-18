#include<stdio.h>
int no_of_children(int row, int col)
{
    int count=0;
    int total = row * col;
    while(row && col)
    {
        count++;
        if(row>col)
            row = row - col;
        else
            col = col - row;
    }
    return count;
}
int main()
{
    int sum=0;
    int minlen,maxlen,minwid,maxwid;
    scanf("%d\n%d\n%d\n%d",&minlen,&maxlen,&minwid,&maxwid);
    if(0<minlen<1501 && 0<maxlen<1501 && 0<minwid<1501 && 0<maxwid<1501)
    {
        for(int i=minlen;i<=maxlen;i++)
        {
            for(int j=minwid;j<=maxwid;j++)
            {
                sum = sum + no_of_children(i,j);
            }
        }
        printf("%d",sum);
    }
    return 0;
}
