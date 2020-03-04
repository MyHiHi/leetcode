# -*- encoding: utf-8 -*-
'''
@File    :   1290. 二进制链表转整数.py
@Time    :   2020/03/04 09:42:45
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   1290. 二进制链表转整数.py
'''

'''
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。
已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

示例 1：

输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
示例 2：

输入：head = [0]
输出：0
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        while head:
            ans=(ans<<1)+head.val;
            # ans<<=1;
            # ans |=head.val
            head=head.next;
        return ans