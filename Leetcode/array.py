a = [6,2,6,5,1,2]
a.sort()
print(a)
print(sum(a))

        
sum(x for x in a if (a.index(x))%2 == 0)




x = 0
sum = 0
while x < len(a):
    min1 = min(a[x], a[x+1])
    sum = sum + min1
    print(sum)
    x += 2