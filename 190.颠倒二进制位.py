# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:56:25 2018
颠倒二进制位：
颠倒给定的 32 位无符号整数的二进制位。
-------------------------------------------------------------------------
示例:
输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
@author: Wan G.S
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int("{0:032b}".format(n)[::-1], 2)    #先将n转化为32位无符号数，然后反转，再返回整数形式

    def reverseBits_2(self, n):
        return int(bin(n).lstrip('0b').zfill(32)[::-1], 2)

    def reverseBits_3(self, n):
        n_list = list('{:032b}'.format(n))
        for i in range(16):
            n_list[i], n_list[31-i] = n_list[31-i], n_list[i]
        res = int(''.join(n_list), 2)
        return res
