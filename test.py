链接：https://www.nowcoder.com/questionTerminal/355885694012495281f415387db22fde?f=discussion
来源：牛客网

//动态规划：#include <bits/stdc++.h>using namespace std;int main(){    vector<int> arr;    while(1){        int t;        cin>>t;        arr.push_back(t);        if(cin.get()=='\n')            break;    }    int n=arr.size();    vector<int> dp(n+1,0);    dp[0]=arr[0];    dp[1]=arr[1];    for(int i=2;i<=n;i++){        dp[i]=min(dp[i-1],dp[i-2])+arr[i];    }    cout<<dp[n];    return 0;} 