# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 11:39:43 2018
前K个高频元素:
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
-------------------------------------------------------
例如，
给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

注意：
你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(nlogn) , n 是数组的大小。
@author: Wan G.S
"""
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in dic[:k]]


if __name__ =="__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3],2))
