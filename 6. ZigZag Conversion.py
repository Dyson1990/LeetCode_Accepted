# -*- coding:utf-8 -*-
"""
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = [[] for i in xrange(numRows)]  # 排在第几排放入第几个列表
        str_l = list(s)
        if numRows <= 1 or len(s) < numRows:
            return s
        
        for i in xrange(len(str_l)):
            """
            若numRows = 4，这么划分为一个区
            x
            x  x
            x x
            x
            """
            num = numRows * 2 - 2  # 每个区域中有多少个字母
            section = i / num  # 自定义区域中第几个区，从0开始
            location = i - num * section  # 自定义区域中，第几个字母
            """
            print 'l初始',l
            print 'i', i
            print 'num',num
            print 'section',section
            print 'location',location
            """
            if location / numRows == 0:
                l[location].append(str_l[i])  # 自定义区域中第一列按顺序放入l
            else:
                l[numRows - 2 - (location - numRows)].append(str_l[i])
                # print 'l完成',l
        
        l_total = []
        for i in xrange(len(l)):
            l_total.append(''.join(l[i]))
        return ''.join(l_total)