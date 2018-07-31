# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:25:26 2018
Shuffle an Array:
打乱一个没有重复元素的数组。
------------------------------------------------------------------
示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
@author: Wan G.S
"""
import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        new = self.nums[:]
        ## random.shuffle(new)
        for i in range(len(new)-1, 0, -1):
            j = random.randrange(0, i+1)
            new[i], new[j] = new[j], new[i]
        return new


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
