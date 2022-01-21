#leetcode problem number : 33
#time complexity: O(logn)
#space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=0;hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid

            #if the first part of  nums is sorted and target lies in first part
            
            if nums[lo]<=nums[mid]:
                
                #check whether the target is in the range of nums[start] to nums[mid]
                if target>=nums[lo] and target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
                
        
            #else, the second part is sorted and the target lies in second part
            
            else:
                if target<=nums[hi] and target>nums[mid]:
                    lo=mid+1
                else:
                    hi=mid-1
                    
                
        return -1
            
            
           
