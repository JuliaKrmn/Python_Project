#https://leetcode.com/problems/climbing-stairs/

#Note: extrimely unfair problem to solve. 
#To see the Fibonacchi pattern in the encreasing number of ways, you had to build a martix of 1 and 2  up to  7 at least. 

class Solution:
    def climbStairs(self, n: int) -> int:
        seq = [0,1]

        for i in range(n):
            seq.append(seq[-1] + seq[-2])

        return seq[len(seq)-1]