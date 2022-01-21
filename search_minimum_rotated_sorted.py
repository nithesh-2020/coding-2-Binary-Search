#leetcode problem number: 153
#time complexity: O(logn)
#space complexity: O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=0 
        n=len(nums)
        lo=0
        hi=n-1
        while(lo<=hi):
            mid=(lo+hi)//2
            if nums[mid]>nums[n-1]: #or we can also check nums[mid]>=nums[0]
                lo=mid+1
            else:
                ans=nums[mid]
                hi=mid-1
        return ans
