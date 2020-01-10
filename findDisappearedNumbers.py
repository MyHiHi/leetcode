# -*- encoding: utf-8 -*-
'''
@File    :   findDisappearedNumbers.py
@Time    :   2020/01/10 10:29:49
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   None
'''

'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]


'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            c=abs(nums[i])-1
            if nums[c]>0:
                nums[c]*=-1;
        print(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if nums[i-1]>0:res+=[i]
        return res

'''
输入
[4,3,2,7,8,2,3,1]
输出
[5,6]
预期结果
[5,6]
stdout
[-4, -3, -2, -7, 8, 2, -3, -1]
'''
