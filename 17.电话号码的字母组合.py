# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 21:00:57 2018
电话号码的字母组合:
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
-------------------------------------------------------------------------
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
@author: Wan G.S
"""
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        if not digits:
            return []
        if len(digits) == 1:
            return dic[digits[0]]
        prev = self.letterCombinations(digits[:-1])
        additional = dic[digits[-1]]
        return [i+j for i in prev for j in additional]



    def letterCombinations_2(self, digits):
        """回溯法"""
        if not digits:
            return []
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        res= []
        self.DFS(digits, dic, 0, '', res)
        return res

    def DFS(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                self.DFS(digits, dic, i+1, path+j, res)
