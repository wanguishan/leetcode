# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:48:37 2018
递增的三元子序列:
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
数学表达式如下:
如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
--------------------------------------------------------------
示例 1:
输入: [1,2,3,4,5]
输出: true

示例 2:
输入: [5,4,3,2,1]
输出: false
@author: Wan G.S
"""
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = [float('inf'), float('inf')]
        for num in nums:
            if num > res[1]:
                return True
            if num <= res[0]:
                res[0] = num
            else:
                res[1] = num
        return False