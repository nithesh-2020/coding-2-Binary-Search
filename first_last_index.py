#leetcode problem : 34
#time complexity: O(logn)
#space complexity: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bisect(nums,target):
            ans=-1
            lo=0;hi=len(nums)-1
            while lo<=hi:
                mid=(lo+hi)//2
                if nums[mid]==target:
                    ans=mid
                    hi=mid-1
                elif nums[mid]<target:
                    lo=mid+1
                else:
                    hi=mid-1
            return ans
        
        def right_bisect(nums,target):
            ans=-1
            lo=0;hi=len(nums)-1
            while lo<=hi:
                mid=(lo+hi)//2
                if nums[mid]==target:
                    ans=mid
                    lo=mid+1
                elif nums[mid]<target:
                    lo=mid+1
                else:
                    hi=mid-1
                
            return ans
        
        lower_bound=left_bisect(nums,target)
        if lower_bound==-1: #this means we can not find lowest index of the element then target is not found in the array. 
            return [-1,-1]
        upper_bound=right_bisect(nums,target)
        return [lower_bound,upper_bound]
