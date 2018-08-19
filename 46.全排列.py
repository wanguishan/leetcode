# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 20:24:43 2018
全排列:
给定一个没有重复数字的序列，返回其所有可能的全排列。
-------------------------------------------------------------
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
@author: Wan G.S
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subList = []
        self.DFS(nums, subList, res)
        return res

    def DFS(self, nums, subList, res):
        if len(subList) == len(nums):
            res.append(subList[:])
        for num in nums:
            if num in subList:
                continue
            subList.append(num)
            self.DFS(nums, subList, res)
            subList.remove(num)