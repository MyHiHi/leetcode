#include<bits/stdc++.h>
using namespace std;
int main(){
  vector<int>arr;
  while (cin.get()!='\n'){
    int t;
    cin>>t;
    arr.push_back(t);
  }
  int n=arr.size();
  vector<int> dp(n+1,0);
  for (int t=2;t<=n;t++){
    dp[t]=min(dp[t-1],dp[t-2])+arr[t]
  }
  cout<<dp[n];
  return 0;
}