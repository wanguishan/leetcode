# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:43:54 2018
颜色分类:
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
-----------------------------------------------------------------------------------------------------------------
示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
@author: Wan G.S
"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        redNums = blueNums = 0
        for index, value in enumerate(nums):
            nums[index] = 1
            if value == 0:
                redNums += 1
            elif value == 2:
                blueNums += 1

        if redNums:
            nums[:redNums] = [0]*redNums
        if blueNums:
            nums[-blueNums:] = [2]*blueNums


    def sortColors_2(self, nums):

        pRed = pWhite = 0
        for index, num in enumerate(nums):
            nums[index] = 2
            if num < 2:
                nums[pWhite] = 1
                pWhite += 1
            if num == 0:
                nums[pRed] = 0
                pRed += 1