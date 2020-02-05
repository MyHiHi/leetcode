# -*- encoding: utf-8 -*-
'''
@File    :   迷路的牛牛.py
@Time    :   2020/02/05 10:31:56
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
题目描述

牛牛去犇犇老师家补课，出门的时候面向北方，但是现在他迷路了。虽然他手里有一张地图，但是他需要知道自己面向哪个方向，请你帮帮他。
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示转方向的次数N(N<=1000)。
接下来的一行包含一个长度为N的字符串，由L和R组成，L表示向左转，R表示向右转。
输出描述:
输出牛牛最后面向的方向，N表示北，S表示南，E表示东，W表示西。

示例1
输入
3
LRR
输出
E
'''
import sys;
c=sys.stdin.readlines();
r=[k.strip() for k in c];
N=int(r[0]);
S=r[1];
# 记录总共向右转了几次，负数也算
coR=0;
# 顺时针编号
direct=['N','E','S','W'];
for i in S:
    if i=='L':coR-=1;
    else:coR+=1;
# 负数取余也是正数：-1%4=3 --> -1-(4)*-1=3
print(direct[coR%4])
