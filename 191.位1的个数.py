# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:10:27 2018
位1的个数:
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
-----------------------------------------------------------------------------------------
示例 :
输入: 11
输出: 3
解释: 整数 11 的二进制表示为 00000000000000000000000000001011
 

示例 2:
输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000
@author: Wan G.S
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## return  sum([((n >> i) & 1) for i in range(32)])
        count =0
        for i in range(32):
            count += (n>>i) & 1
        return count
        
    def hammingWeight_2(self, n):
        return bin(n).count('1')

    def hammingWeight_3(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count