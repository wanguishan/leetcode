# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:38:12 2018
缺失数字:
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
--------------------------------------------------------------------------------
示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
@author: Wan G.S
"""
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)//2 - sum(nums)


    def missingNumber_2(self, nums):
        """
        时间复杂度O(n)
        空间复杂度O(1)
        """
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= (i^num)
        return res
