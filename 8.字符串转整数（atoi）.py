# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:13:23 2018
字符串转整数（atoi:
实现 atoi，将字符串转为整数。
-------------------------------------------------------------------
示例 1:
输入: "42"
输出: 42

示例 2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
     
示例 3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例 4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
     
示例 5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。
@author: Wan G.S
"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ls = list(str.strip())
        if not ls:
            return 0
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+']:
            del ls[0]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            res = res*10 + int(ls[i])
            i += 1
        return max(-2**31, min(sign * res,2**31-1))         