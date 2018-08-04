# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 19:02:01 2018
岛屿的个数:
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3
@author: Wan G.S
"""
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(grid, i, j)
                    count += 1
        return count

    def DFS(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = 0
            self.DFS(grid,i-1, j)
            self.DFS(grid,i+1, j)
            self.DFS(grid,i, j-1)
            self.DFS(grid,i, j+1)