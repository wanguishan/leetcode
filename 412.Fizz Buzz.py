# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:30:44 2018
Fizz Buzz：
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
---------------------------------------------------------------
示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
@author: Wan G.S
"""
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if i%3 ==0 and i%5 == 0:
                res.append('FizzBuzz') 
            elif i%3 == 0:
                res.append('Fizz')
            elif i%5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


    def fizzBuzz_2(self, n):
        res = []
        for i in range(1, n+1):
            temp = ''
            if i%3 == 0:
                temp += 'Fizz'
            if i%5 == 0:
                temp += 'Buzz'
            if temp == '':
                temp += str(i)
            res.append(temp)
        return res
    
    
if __name__ == '__main__':  
    print(Solution().fizzBuzz(15))      
    print(Solution().fizzBuzz_2(15))    
            
