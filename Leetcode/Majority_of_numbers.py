#https://leetcode.com/problems/majority-element/

nums = [3,2,3]

half = len(nums)/2

print (half)

res = []

for item in nums:
    if item not in res:
        res.append(item)

print(res)

i = 0
for  i  in  range (len(nums)):
    count =nums.count(res[i])

    if count >= half:
        print (res[i])
        break
   
