#https://leetcode.com/problems/valid-palindrome/

s = "A man, a canal: Panama"
s = s.lower()

r = ''.join([char for char in s if char.isalnum()])

r = s[::-1]

if s == r:
    print(f"{s} is a palindrome.")
else:
    print (f"{s} is not a palindrome.")

