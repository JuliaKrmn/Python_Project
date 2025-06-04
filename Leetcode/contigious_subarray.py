nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
print(len(nums))
print(nums.count(0))
print(nums.count(1))

# Start from the first index
i = 0
solution = [] 
while i < len(nums):
    fix = nums[i:(len(nums))]
    if fix.count(0) == fix.count(1): 
        solution.append(fix)
        
    i += 1


nums.reverse()

j= 0
while j < len(nums):
    fix = nums[j:(len(nums))]
    if fix.count(0) == fix.count(1): 
        solution.append(fix)
      
    j += 1

print(solution)

if len(solution) > 0: 
    l = max(solution, key = len)

    print(len(l))

else: 
    print(0)
# solution = []
# r = 0 
# for x in len(nums): 

#     if nums.count(0) == nums.count(1): 
#         solution.append(r)




#nums[n] = range(n) 

# nums1 = range(9)
# a = list(nums1)
# print(a)