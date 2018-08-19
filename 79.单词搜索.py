# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 21:44:27 2018
单词搜索：
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
-------------------------------------------------------------------------------------------
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
@author: Wan G.S
"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.DFS(board, i, j, word):
                        return True
        return False

    def DFS(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        res = self.DFS(board, i-1, j, word[1:]) or self.DFS(board, i+1, j, word[1:]) \
        or self.DFS(board, i, j-1, word[1:]) or self.DFS(board, i, j+1, word[1:])
        board[i][j] = temp
        return res