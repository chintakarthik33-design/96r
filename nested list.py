l=[1,2,3,],[4,5],[6,7]
print(l[0])
l1=[1,2,3,4,5,6,7]
print(l1[0])
l2=[[1,2,3],[4,5,6],[7,8,9]]
print(l2[0][0])# 1 2d index
l[0][0]# list(index(inside(index)))
l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[0][0])
print(l[2][1])
print(l[1][2])
#slicing nested 
l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[0:2])
l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1[0:2])
print(l1[0][1:5])
print(l1[1][2:5])

# using loops
# loop1 acceses outer part [1,2,3],[4,5,6],[7,8,9]
# loop2 nested loop 1,2,3,4,5,6,7,8
l=[[1,2,3],[4,5,6],[6,7,8]]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])
l=[[1,2],[3,4,[5,6]]]
print(l[1][2][1])

l=[1,2,3,["ravi","raju"],[4,5]]
for i in range(len(l[3])):
    print(l[3][i])
l=[1,2,3],[4,5,6],[7,8,9]
for i in range (len(l)):
    sum=0
    for j in range(len(l[i])):
        sum+=l[i][j]
    print(sum)
