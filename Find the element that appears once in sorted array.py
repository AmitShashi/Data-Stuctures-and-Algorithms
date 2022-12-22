#Find the element that appears once in sorted array. ( All other elements appear exactly twice. )
class Solution:
    def findOnce(self, arr : list, n : int):

        res=0
        for i in arr:
            res=res^i
        
        return res
