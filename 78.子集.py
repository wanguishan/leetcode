# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 21:10:07 2018
子集：
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
----------------------------------------------------------------
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
@author: Wan G.S
"""
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        s = []
        self.DFS(nums, s, 0)
        return self.res

    def DFS(self, nums, s, index):
        if len(nums) == index:
            self.res.append(s)
            return
        self.DFS(nums, s+[nums[index]], index+1)
        self.DFS(nums, s, index+1)
