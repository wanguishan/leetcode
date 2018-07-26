# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:41:36 2018
二分查找
--------------------------------------------
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
@author: Wan G.S
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p1, p2 = 0, len(nums)-1
        while p1<=p2:
            pMid = (p1+p2)//2
            if nums[pMid] < target:
                p1 = pMid + 1
            elif nums[pMid] > target:
                p2 = pMid -1
            else:
                return pMid
        return -1
                
    

