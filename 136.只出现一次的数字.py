# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:41:53 2018
只出现一次的数字：
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
-----------------------------------------------
示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
@author: Wan G.S
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        异或操作^: x^x=0, 0^x=x  ----> ((A^A) ^ (B^B) ^ (C^C) ^ (D^D) ^ E) = ((0^ 0 ^ 0 ^ 0 ^ E) =E
        """
        result = 0
        for i in nums:
            result = result^i
        return result
    
        
        

