import numpy


nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]

n = len(nums)
res = []
biggest = 0


print(biggest)
#------

# for i in range(n):

#     for j in range(i + 1, n + 1):

#         if nums[i:j].count(0) == nums[i:j].count(1):

#             res.append(nums[i:j])

#             l = max(res, key = len)

#             biggest.clear()
#             biggest.append(l)

for i in range(n):
    for j in range(i + 1, n + 1):

        if len(nums[i:j])%2 == 0: 

            if nums[i:j].count(0) == nums[i:j].count(1):    

                if len(nums[i:j]) > biggest: 
                
                    
                    biggest = len(nums[i:j])                

            
print(biggest)

   
# #print(res)

# if len(biggest) > 0: 

#     print(len(biggest[0]))

# else: 
#     print(0)


#----

            #     l = max(res, key = len)

            # if len(nums[i:j]) < len(l):
            #     res.remove(nums[i:j])