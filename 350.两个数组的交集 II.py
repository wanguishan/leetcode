# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:23:59 2018
两个数组的交集 II：
给定两个数组，写一个方法来计算它们的交集。
-----------------------------------
例如:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
@author: Wan G.S
"""
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}    #用来记录nums里每个元素出现的次数
        res = []
        for i in nums1:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
          # count[i] = count.get(i, 0) + 1    #简单写法
        for j in nums2:
            if j in count and count[j] > 0:
                res.append(j)
                count[j] -= 1
        return res
