from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        a = [s]
        jl = []
        for list in queries:
            new = []
            start = list[0]
            stop = list[1]
    
    
            new.append(a[start:stop+1])

            if new[0].count("|") < 2: 

                jl.append(0)

            else: 

                first = new[0].index('|')


                last = len(new[0]) - 1 - new[0][::-1].index("|")


                validation_array = new[0][first:last]


                jl.append(validation_array.count("*"))
    
   
      
        return jl


if __name__ == '__main__':
    sol = Solution()
    
    s = "||***|"
    queries = [[2,5],[5,9]]

    print(sol.platesBetweenCandles(s,queries))

    s = "***||*****|||**|*"
    queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]

    print(sol.platesBetweenCandles(s,queries))