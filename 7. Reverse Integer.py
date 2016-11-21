"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = x / abs(x) # 正负号
        s = str(abs(x))
        s = s[::-1]
        return int(s) * sign

