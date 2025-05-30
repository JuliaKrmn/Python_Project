#https://leetcode.com/problems/search-insert-position/description/

nums =[1]
target = 0

# class Solution(object):
#     def searchInsert(self, nums, target):
"""
:type nums: List[int]
:type target: int
:rtype: int
"""
    
if target in nums: 
    index = nums.index(target)
    print(index)

else: 
   for i in range (len(nums)):
        if nums[i-1]  < target < nums[i]:
            print(i)
        
        elif target > nums[-1]:
            print (len(nums))
            break

        elif target < nums[0]:
            print(0)
            break 




        
# #    print(nums.index(target-1) < nums.index(target) < nums(target+1))
#     # nums[0] nums.index(target) nums[1]    
#         x = nums.insert(3, target)  
#         print(nums)

from typing import List
 
 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)
 
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums=[1,3,5,6],target=6))
 
    print(s.searchInsert(nums=[1,3,5,6],target=2))
 
    print(s.searchInsert(nums=[1,3,5,6],target=7))