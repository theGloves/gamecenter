# -*- coding:utf-8 -*-
# author: ljj ruc
#
# 五子棋类
import os


class Gobang(object):
    def __init__(self):
        self.size = 15
        # 初始化棋盘
        self.__board = [[0 for n in range(self.size)]
                        for m in range(self.size)]
        self.id = 0

    # 胜利条件
    def is_end(self):
        ch_stack = []
        # 行检查
        for i in range(self.size):
            for j in range(self.size):
                # 判断是否结束
                chess = self.__board[i][j]
                if len(ch_stack) == 5 and ch_stack[-1] == 1:
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == 2:
                    return 2
                if chess == 0:
                    ch_stack.clear()
                else:
                    if (not ch_stack) or ch_stack[-1] == chess:
                        ch_stack.append(chess)
                    else:
                        ch_stack.clear()
                        ch_stack.append(chess)
            ch_stack.clear()
        ch_stack.clear()
        # 列检查
        for j in range(self.size):
            for i in range(self.size):
                # 判断是否结束
                if len(ch_stack) == 5 and ch_stack[-1] == 1:
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == 2:
                    return 2
                chess = self.__board[i][j]
                if chess == 0:
                    ch_stack.clear()
                else:
                    if (not ch_stack) or ch_stack[-1] == chess:
                        ch_stack.append(chess)
                    else:
                        ch_stack.clear()
                        ch_stack.append(chess)
            ch_stack.clear()
        ch_stack.clear()
        # 左斜检查
        # 下三角
        for i in range(self.size):
            for j in range(1, self.size):
                # 判断是否结束
                if len(ch_stack) == 5 and ch_stack[-1] == 1:
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == 2:
                    return 2

                if i+j < self.size:
                    chess = self.__board[i+j][j]
                    if chess == 0:
                        ch_stack.clear()
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
        # 上三角
        for i in range(self.size):
            for j in range(1, self.size):
                # 判断是否结束
                if len(ch_stack) == 5 and ch_stack[-1] == 1:
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == 2:
                    print('winner=id 2')
                    return 2
                if i+j < self.size:
                    chess = self.__board[j][j+i]
                    if chess == 0:
                        ch_stack.clear()
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
        # 右斜检查
        # 上三角
        for i in range(self.size):
            for j in range(1, self.size):
                # 判断是否结束
                if len(ch_stack) == 5 and ch_stack[-1] == 1:
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == 2:
                    return 2
                if self.size-i-j+1 > 0:
                    chess = self.__board[self.size-i-j][j]
                    if chess == 0:
                        ch_stack.clear()
                    elif not chess:
                        break
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
        # 下三角
        for i in range(self.size):
            for j in range(1, self.size):
                # 判断是否结束
                if len(ch_stack) == 5 and ch_stack[-1] == 1:
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == 2:
                    return 2
                if self.size-i-j > 0:
                    chess = self.__board[j][self.size-i-j]
                    if chess == 0:
                        ch_stack.clear()
                    elif not chess:
                        break
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
        return 0

    def drop_chess(self, x, y, id):
        if id == 1 and self.__board[x][y] == 0:
            self.__board[x][y] = 1
            return 1
        elif id == 2 and self.__board[x][y] == 0:
            self.__board[x][y] = 2
            return 1
        else:
            return 0

    def chess_status(self):
        return self.__board