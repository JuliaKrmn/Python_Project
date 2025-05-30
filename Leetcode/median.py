#https://leetcode.com/problems/median-of-two-sorted-arrays/

import statistics
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        return statistics.median(nums3)
    

# Arrange data values from lowest to highest value
# The median is the data value in the middle of the set
# If there are 2 data values in the middle the median is the mean of those 2 values.

# class Solution2:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         pass
nums1 = list()
nums2 = list()
nums_united = [0,1,2,3,4,5,6,7,8,9,10]

if len(nums_united)%2 == 1:
    index = (len(nums_united)-1)/2 
    print(nums_united[index])

else:
    index1 = len(nums_united)/2 
    index2 = len(nums_united)/2 +1

    print((nums_united[index1] + nums_united[index2])/2)



#--------------------------------------------------
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_united = nums1+nums2
        nums_united.sort()

        if len(nums_united)%2 == 1:
            index = int((len(nums_united)-1)/2 )
            return nums_united[index]

        else:
            index1 = int(len(nums_united)/2 )
            index2 = int(len(nums_united)/2 - 1)

            return float((nums_united[index1] + nums_united[index2])/2)