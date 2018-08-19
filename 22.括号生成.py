# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 19:56:14 2018
生成括号：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
------------------------------------------------------------------------------
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
@author: Wan G.S
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def DFS(left, right, st, res):
            if left == 0 and right == 0:
                res.append(st)
            else:
                if left > 0:
                    DFS(left-1, right, st+'(', res)
                if right > left:
                    DFS(left, right-1, st+')', res)

        res = []
        DFS(n, n, '', res)
        return res

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
