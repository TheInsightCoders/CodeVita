import java.util.*;
public class CandiesProblem{
	public  static  void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			PriorityQueue<Integer> pq=new PriorityQueue<Integer>();
			for(int i=0;i<n;i++){
			//	arr[i]=sc.nextInt();
			pq.add(sc.nextInt());
			
			}
			int ans=0;
			while(pq.size()>1){
				int temp=pq.poll();
				temp+=pq.poll();
				ans+=temp;
				pq.add(temp);
				
			}
			System.out.println(ans);
	
		
	}
	}
	 
	
}