# -*- coding:utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
用python简单很多，优化好的，用c的话，TLE的限制可能会有些难
另外，我没有用numpy中的中位数函数，估计比我下面写的更快吧
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums = sorted(nums1)
        print 'nums', nums
        len0 = len(nums)
        if len0 % 2 == 0:
            return (nums[len0 / 2 - 1] + nums[len0 / 2]) / 2.0
        else:
            return nums[int(len0 / 2)]
