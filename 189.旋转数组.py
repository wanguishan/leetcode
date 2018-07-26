# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:53:34 2018
旋转数组：
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
-------------------------------
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
@author: Wan G.S
"""
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]    #注意 nums[:] 不可以换成 nums[]
        
    def rotate_2(self, nums, k):
        for i in range(k):
            nums.insert(0, nums.pop(-1))
        
    def rotate_3(self, nums, k):
        """空间复杂度为O(1)"""
        k = k % len(nums)

        self.reverse(nums, 0, len(nums)-1-k)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)        
    def reverse(self, nums, p1, p2):
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1
        
        
