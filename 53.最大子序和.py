# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:20:24 2018
最大子序和:
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
------------------------------------------------------------------------------
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
@author: Wan G.S
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = float('-inf')
        for num in nums:
            curSum = max(num+curSum, num)
            maxSum = max(curSum, maxSum)
        return maxSum


    def maxSubArray_2(self, nums):
        """ 
        动态规划法，时间复杂度O(n)        
        """
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > maxSum:
                maxSum = nums[i]
        return maxSum
