#https://leetcode.com/problems/string-to-integer-atoi/

import sys

class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        d = []
     
        if s == "":
            return 0

        if s[0] == "+" or s[0] == '-':

            new_string = s
            d.append(s[0])
      

            for x in new_string[1:]: 
    
                if x.isnumeric():
                    d.append(x)
                    continue
                else:
                    break 
                   

        else: 
    
            for x in s: 
    
                if x.isnumeric():
            
                    d.append(x)
                    continue

                else:
                    break  

        max = 2147483647
        min = -2147483648

        if d == ['+'] or d == ['-'] or d == []:
            return 0 
        
  
        else: 

            res = ''.join(d)



            if min <= int(res) <= max: 
                return int(res)


            if int(res) < min:
                return int(min)

            if int(res)> max: 
                return int(max)

        