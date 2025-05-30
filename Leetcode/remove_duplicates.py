#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

nums = [0,0,1,1,1,2,2,3,3,4]
print (nums)

mylist = list(dict.fromkeys(nums))

nums.clear()

nums.extend(mylist)

k = len(mylist)

print(mylist)
print(nums)
print(type(mylist))

