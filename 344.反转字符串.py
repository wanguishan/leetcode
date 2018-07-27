# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:42:50 2018
反转字符串：
请编写一个函数，其功能是将输入的字符串反转过来。

示例：
输入：s = "hello"
返回："olleh"
@author: Wan G.S
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            s[p1],s[p2] = s[p2],s[p1]
            p1 +=1
            p2 -=1
        return ''.join(s)
    
    def reverseString_2(self, s):
        return s[::-1]
        
    def reverseString_3(self, s):
        if len(s) <= 1:
            return s
        n = len(s)
        return self.reverseString_3(s[n//2:]) + self.reverseString_3(s[:n//2])


if __name__ == '__main__':
    s = 'hello'
    print(Solution().reverseString(s))   
    print(Solution().reverseString_2(s))   
    print(Solution().reverseString_3(s))       