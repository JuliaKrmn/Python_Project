#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import itertools
class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sum = []
        sum2= []

        combinations1 = list(itertools.product(nums1,nums2))


        for x in combinations1: 
            sum.append([x[0] + x[1], list(x)])
            
            sum.sort()

         

        for x in range(k):
            sum2.append(sum[x][1])


        return sum2