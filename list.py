# l=[10,20,30,40,50]
# l.append(70)#append
# print(l)

# l.insert(2,"hi")
# print(l)
# # l1=[1,2,3]
# # l.extend(l1)
# # print(l)
# print(l.pop())
# print(l.pop(2))
# l.remove(20)
# print(l)
# # l2=l.copy()
# # print(l2)
# print(l.count(10))
# l.reverse()
# print(l)
# l.sort()
# # print(l)
# l=["banana","grapes","guva"]
# l.sort()
# print(l)
# l=[10,20,30,40]
# l.clear()
# print(l)
# l=[10,20,30,40]
# print(l.index(10))
# l=["apple","banana","guva","atipandu"]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l1=[1,2,3]
# l2=[4,5,6]
# l=l1+l2
# l3=l1*2
# print(l3)

# #MAX
l=[10,20,30,40,50]
max1=0
for i in range (len(l)):
    if(max1<l[i]):
        max1=l[i]
print(max1)
#WITH OUT RANGE FUNCTION 
l=[10,20,30]
max1=0
for val in l:
    if max1<val:
        max1=val
print(max1)
#MIN
l=[10,20,30,40,50]
min1=l[0]

for i in range (len(l)):
    if min1>l[i]:
        min1 = l[i]
print(min1)
# SUM OF VALUES
l=[10,20,30,40,50]
total=0
for val in l:
    total+=val
print(total)
#PRODUCT OF LIST'
l=[10,20,30,40]
product=0
for val in l:
    product+=val
print(product)
#LENGth count OF LIST
l=[10,20,30,40,50]
count=0
l.count(l)
for val in l:
    count+=1
print(count)