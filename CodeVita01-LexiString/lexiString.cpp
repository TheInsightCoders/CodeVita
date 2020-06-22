#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int n;
	cin>>n;
	
	
	 
	while(n!=0)
	{ string p,s;
	  vector<int> v;
		cin>>p;
		cin>>s;
		
		for(int i=0;i<s.size();i++)
		{
			for(int j=0;j<p.size();j++)
			{
				if(s[i]==p[j])
				{
					v.push_back(j);
				}
			}
		}
		sort(v.begin(),v.end());
	
	for(int i=0;i<v.size();i++)
	{
		cout<<p[v[i]];
	}
	
		n--;
    } 
	

	
}
