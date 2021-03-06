# -*- encoding: utf-8 -*-
'''
@File    :   跳 1 或 2 个格子,不同的方法数到终点.py
@Time    :   2020/03/13 09:56:16
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   跳 1 或 2 个格子,不同的方法数到终点.py
'''

'''
题目描述
假设你正在玩跳格子（所有格子排成一个纵列）游戏。需要 跳完n 个格子你才能抵达终点。
每次你可以跳 1 或 2 个格子。你有多少种不同的方法可以到达终点呢？
注意：给定 n 是一个正整数。
输入描述:
格子数n
输出描述:
跳完n个格子到达终点的方法
示例1
输入
2
输出
2
'''
n=int(input());
dp=[0]*(n+1);
dp[1]=1;
dp[2]=2;
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])