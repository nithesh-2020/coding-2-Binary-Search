#leetcode problem no. : 702
#time complexity : O(logn)
#space complexity: O(1)

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        #see in this question I can maske use of the constraints and take the higher bound value 
        #but here in the problem, it is given to solve the problem in O(logn)
        #but the time complexity of my problem is O(N)
        
        if reader.get(0)==target:
            return 0
        
        #Search for boundaries
        
        left,right=0,1
        while reader.get(right)<target:
            left=right
            right=right*2 #at each iteration m
        # print(left,right)
        #perform binary search
        while left<=right:
            mid=(left+right)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        return -1
        
        
