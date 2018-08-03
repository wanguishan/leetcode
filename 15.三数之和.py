# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:19:18 2018
三数之和：
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
----------------------------------------------------------------------------------
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
@author: Wan G.S
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        > 时间复杂度O(n^2)
        > 空间复杂度O(1)
        """
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:    # i去重
                continue
            else:
                left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:    # left去重
                        left += 1
                    while left<right and nums[right] == nums[right+1]:    # right去重
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res


