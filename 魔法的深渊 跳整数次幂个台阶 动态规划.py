# -*- encoding: utf-8 -*-
'''
@File    :   魔法的深渊.py
@Time    :   2020/02/20 10:42:29
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   魔法的深渊.py
'''

'''
题目描述
前几个月放映的头号玩家简直火得不能再火了，作为一个探索终极AI的研究人员，月神自然去看了此神剧。
由于太过兴奋，晚上月神做了一个奇怪的梦，月神梦见自己掉入了一个被施放了魔法的深渊，月神想要爬上此深渊。

已知深渊有N层台阶构成（1 <= N <= 1000)，并且每次月神仅可往上爬2的整数次幂个台阶(1、2、4、....)，请你编程告诉月神，月神有多少种方法爬出深渊
输入描述:
输入共有M行，(1<=M<=1000)

第一行输入一个数M表示有多少组测试数据，

接着有M行，每一行都输入一个N表示深渊的台阶数
输出描述:
输出可能的爬出深渊的方式
示例1
输入
4
1
2
3
4
输出
1
2
3
6
备注:
为了防止溢出，可将输出对10^9 + 3取模
'''
'''
台阶问题考虑动态规划
每次仅可往上爬2的整数次幂个台阶(1、2、4、....)
当前台阶方法数 = 所有一次可到达当前台阶方法数的和
dp[n] = dp[n-1]+dp[n-2]+dp[n-4]+... ( n-t>=0,dp[0]=1 )
'''
M=int(input().strip());
mod=1e9+3;
p=[1]+[0]*1000;
for i in range(1,1001):
  t=1;
  while t<=i:
    p[i]+=p[i-t];
    p[i]=int(p[i]%mod);
    t*=2;
for _ in range(M):
  i=int(input().strip());
  print(p[i])