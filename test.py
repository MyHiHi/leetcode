X=int(input())
dp=[1000 for _ in range(X+1)];
dp[3],dp[5],dp[6],dp[7]=1,1,2,1
for i in range(8,X+1):
    dp[i]=min(dp[i-3],min(dp[i-5],dp[i-7]))+1;
print(-1 if dp[X]>=1000 else dp[X])