#https://leetcode.com/problems/3sum/

import itertools
from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        seen = defaultdict(int)
        result = []

        for num in nums:
            if seen[num] < 2:
                result.append(num)
                seen[num] += 1



        newest_list = []

        new_list = list(itertools.combinations(result, 3))

        unique_items = list(dict.fromkeys(new_list))

        for x in unique_items:

            sum = x[0] + x[1] + x[2]

            if sum == 0:

                newest_list.append(list(x))

        unique_items1 = []

        for x in newest_list:

            x.sort()

            if x not in unique_items1:

                unique_items1.append(x)

        return unique_items1

