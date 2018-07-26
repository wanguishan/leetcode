# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:56:07 2018
两数之和：
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
--------------------------------------------------------
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
@author: Wan G.S
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i, num in enumerate(nums):
            if target-num not in res:
                res[num] = i
            else:
                return [res[target-num], i]

            

                

                
                
            

            
            

