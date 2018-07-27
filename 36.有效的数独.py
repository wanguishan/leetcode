# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:33:28 2018
有效的数独：
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用 '.' 表示。
https://leetcode.com/problems/valid-sudoku/description/
@author: Wan G.S
"""
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        暴力法
        """
        for i in range(9):
            if 9 - len(set(board[i])) != board[i].count('.') -1:
                return False
            
            new_list = []
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in new_list:
                    return False
                if board[j][i] != '.' and board[j][i] not in new_list:
                    new_list.append(board[j][i])

              
        aa, bb = [0, 3, 6], [0, 3, 6]
        for a in aa:
            for b in bb:
                new_list = []
                for i in range(a, a+3):
                    for j in range(b, b+3):
                        if board[j][i] != '.' and board[j][i] in new_list:
                            return False
                        if board[j][i] != '.' and board[j][i] not in new_list:
                            new_list.append(board[j][i])          
        return True
#==================================================================================================    
    def isValidSudoku_2(self, board):
        """思路2"""
         rows = [{},{},{},{},{},{},{},{},{}]
         cols = [{},{},{},{},{},{},{},{},{}]    
         boxes = [{},{},{},{},{},{},{},{},{}] 
         
         for i in range(9):
             for j in range(9):
                 num = board[i][j]
                 if num == '.':
                     continue
                 else:
                     if num not in rows[i] and num not in cols[j]  and num not in boxes[3*(i//3) + (j//3)]:
                         rows[i][num] = 1
                         cols[j][num] = 1
                         boxes[3*(i//3) + (j//3)][num] = 1
                     else:
                         return False
         return True
     
#===================================================================================================       
    def isValidSudoku_3(self, board):
        """思路2的Pythonic写法"""
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        boxes = [[] for i in range(9)]
        
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    if num in rows[i] + cols[j] + boxes[3*(i//3)+(j//3)]:
                        return False
                    rows[i].append(num)
                    cols[j].append(num)
                    boxes[3*(i//3)+(j//3)].append(num)
        return True      
         
         
         
if __name__ == '__main__':
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))
    print(s.isValidSudoku_2(board))         
    print(s.isValidSudoku_3(board))          