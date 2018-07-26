# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:04:25 2018
存在重复：
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
---------------------------------------------
示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
@author: Wan G.S
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)
    
    

    def containsDuplicate_2(self, nums):

        new = set()
        for num in nums:
            if num not in new:
                new.add(num)
            else:
                return True
        return False

        