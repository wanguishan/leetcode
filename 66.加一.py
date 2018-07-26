# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:50:36 2018
加一：
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
----------------------------

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
@author: Wan G.S
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_digits = int(''.join('%s' %i for i in digits))      
        int_digits += 1
        str_int_digits = str(int_digits)
        res = []
        for i in str_int_digits:
            res.append(int(i))
        return res
    
    def plusOne_2(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits)-1-i)
        return [int(i) for i in str(num+1)]
            
if __name__ == '__main__':
     s = Solution()
     digit = [9,9,9]
     print(s.plusOne(digit))
     print(s.plusOne_2(digit))       
