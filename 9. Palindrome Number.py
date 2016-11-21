"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if len(s) == 1:
            return True
            
        if len(s) % 2 == 0:
            s1 = s[:len(s)/2]
            s2 = s[len(s)/2:][::-1]
            print s1
            print s2
        else:
            s1 = s[:int(len(s)/2)]
            s2 = s[int(len(s)/2) + 1:][::-1]
        if s1 == s2:
            return True
        else:
            return False

