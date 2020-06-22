import java.util.Scanner;
import java.util.*;

public class LexiString{

public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
StringBuffer sb=new StringBuffer();
while(n-->0)
{
String p=sc.next()+sc.nextLine();
String s=sc.next()+sc.nextLine();
sb.append(lexi(p,s)+"\n");
}
System.out.print(sb);

}

private static String lexi(String p, String s) {
String result="";
TreeSet<Integer> set = new TreeSet<>(); 
for(int i=0;i<s.length();i++)
{
int index=p.indexOf(s.charAt(i));
if(set.contains(index))
{
for(int j=index;j<=(p.lastIndexOf(s.charAt(i)));j++)
{
int in=p.indexOf(s.charAt(i),j);
if(set.contains(in))
continue;
else
set.add(in);
}
}
else
set.add(index);
}
for(int i:set)
result=result+p.charAt(i);
return result;
}

}