# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:53:34 2018
矩阵置零：
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
--------------------------------------------------------------------------------
示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
@author: Wan G.S
"""
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        > 空间复杂度O(m*n)
        """
        index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    index.append((i, j))

        for row, col in index:
            matrix[row] = [0] * len(matrix[0])
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return



    def setZeroes_2(self, matrix):
        """空间复杂度O(m+n)"""
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            matrix[row] = [0] * len(matrix[0])
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return

