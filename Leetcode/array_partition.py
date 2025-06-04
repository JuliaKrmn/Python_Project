
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        biggest = 0
        x = 0
        sum = 0
        while x < len(nums):
            min1 = min(nums[x], nums[x+1])
            sum = sum + min1
            x += 2

            if sum < 0: 
                biggest = sum

            if sum > biggest: 
                biggest = sum 

        return biggest
