# -*- encoding: utf-8 -*-
'''
@File    :   530. 二叉搜索树的最小绝对差.py
@Time    :   2020/03/12 11:13:16
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   530. 二叉搜索树的最小绝对差.py
'''

'''
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res=10000
        self.prev=None
        def inOrder(root):
            if root==None:return ;
            inOrder(root.left);
            if self.prev:
                self.res=min(self.res,abs(self.prev.val-root.val));
            self.prev=root;
            inOrder(root.right);
        inOrder(root);
        return self.res