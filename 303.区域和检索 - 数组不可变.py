# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:05:20 2018
区域和检索 - 数组不可变:
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
-----------------------------------------------------------------------------------
示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
@author: Wan G.S
"""
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = []
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            self.dp.append(curSum)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]



# =============================================================================
# class NumArray:
#     def __init__(self, nums):
#         self.DP = nums
#         for i in range(1, len(nums)):
#             self.DP[i] += self.DP[i-1]
#
#
#     def sumRange(self, i, j):
#         return self.DP[j] - (self.DP[i-1] if i > 0 else 0)
# =============================================================================
