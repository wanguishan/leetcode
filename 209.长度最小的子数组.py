# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:18:54 2018
长度最小的子数组：
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。
----------------------------------------------------------------------------------------
示例:
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
@author: Wan G.S
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        >> 时间复杂度O(n)，空间复杂度O(1)
        """
        start = 0
        end = -1
        sum = 0
        res = float('inf')
        while start < len(nums):
            if sum < s and end < len(nums)-1:
                end += 1
                sum += nums[end]
            else:
                sum -= nums[start]
                start += 1
            if sum >= s:
                res = min(res, end-start+1)
        if res > len(nums):
            return 0
        return res

    def minSubArrayLen_2(self, s, nums):
        sum = start = 0
        res = float('inf')
        for end, num in enumerate(nums):
            sum += num
            while sum >= s:
                res = min(res, end-start+1)
                sum -= nums[start]
                start += 1
        if res > len(nums):
            return 0
        return res
