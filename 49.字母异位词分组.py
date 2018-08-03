# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 13:26:41 2018
字谜分组:
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
------------------------------------------------------------------------------
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
@author: Wan G.S
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            s_sort = ''.join(sorted(s))
            if s_sort not in dic:
                dic[s_sort] = [s]
            else:
                dic[s_sort].append(s)    # dic[s_sort] += [s]

  ##写法2： dic.setdefault(s_sort, []).append(s)
  ##写法3： dic[''.join(sorted(s))] = dic.get(s_sort, []) + [s]
        return list(dic.values())

if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
