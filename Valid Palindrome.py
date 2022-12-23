'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
class Solution(object):
    def isPalindrome(self, s):

        res=[]
        for i in s:
            if i.isalnum() :
                res.append(i.lower())
        
        s1=join(res)
        s2=s1[::-1]
        if s1 == s2: return True
        else: return False
