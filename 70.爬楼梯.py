# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:03:00 2018
爬楼梯：
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
---------------------------------------------------------------------------
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步
@author: Wan G.S
"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


    def climbStairs_2(self, n):
        """
	动态规划法 f(n) = f(n-1) + f(n-2)
	"""
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
