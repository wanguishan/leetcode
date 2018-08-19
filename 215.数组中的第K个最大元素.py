# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 20:03:01 2018
数组中的第K个最大元素:
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
-------------------------------------------------------------------------------------------------------
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
@author: Wan G.S
"""
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        small, pivotList, large = [], [], []
        pivot = nums[0]
        for num in nums:
            if num < pivot:
                small.append(num)
            elif num > pivot:
                large.append(num)
            else:
                pivotList.append(num)

        if k <= len(large):
            return self.findKthLargest(large, k)
        elif k-len(large) <= len(pivotList):
            return pivotList[0]
        else:
            return self.findKthLargest(small, k-len(large)-len(pivotList))




nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, 2))
