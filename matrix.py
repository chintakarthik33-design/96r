# l=[[1,2,3],[4,5,6]]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j],end=" ")
#         print()
# l1=[[1,2,3],[4,5,6]]
# l2=[[7,8,9],[6,5,4]]
# for i in range(len(l1)):
#     for j in range(len(l1[i])):
#         print(l1[i][j],end=" ")
#     print( )

# sum of matrix or eddition matrix 

# l1=[[1,2,3],[4,5,6],[7,8,9]]
# l2=[[9,8,7],[6,5,4],[3,2,1]]
# l3=[]

# for i in range (len(l1)):
#     l=[]
#     for j in range(len(l1[i])):
#         add=l1[i][j]+l2[i][j]
#         l.append(add)
#     l3.append(l)
# for i in range(len(l3)):
#     for j in range(len(l3[i])):
#         print(l3[i][j],end=" ")
#     print()

# multiple matrix

# l1=[[1,2],[3,4]]
# l2=[[4,3],[2,1]]
# l3=[]
# for i in range(len(l1)):
#     l=[]
#     for j in range(len(l1[i])):
#         add=0
#         for k in range(len(l1[i])):
#             add=add+(l1[i][k]*l2[k][j])
#         l.append(add)
#     l3.append(l)
#     for i in range(len(l3)):
#         for j in range(len(l3[i])):
#             print(l3[i][j],end=" ")
#         print()




# l1=[[1,2,3],[4,5,6]] # 2x3
# l2=[[3,2],[2,1],[1,4]] # 3x2 - Changed this
# l3=[]
# for i in range(len(l1)):
#     l=[]
#     for j in range(len(l2[0])):
#         add=0
#         for k in range(len(l1[0])): #  Change len(l) to len(l1[0]) or len(l2)
#             add=add+(l1[i][k]*l2[k][j])
#         l.append(add) #  This should be outside k loop
#     l3.append(l)

# transpose of matrix columns to rows and rows to columnss

# l1=[[1,2,3],[4,5,6]]
# transpose=[]
# for i in range(len(l1[0])):
#     row=[]
#     for j in range(len(l1)):
#         row.append(l1[i][j])
#     transpose.append(row)
# print(transpose)
# Original matrix - 2x3
# matrix = [[1,2,3],[4,5,6]]
# transpose = []

# # rows become columns, columns become rows
# for i in range(len(matrix[0])): # 3 columns → 3 rows in transpose
#     row = []
#     for j in range(len(matrix)): # 2 rows → 2 columns in transpose
#         row.append(matrix[j][i]) # Swap i and j
#     transpose.append(row)

# print(transpose)
l1=[[1,2,3],[4,5,6]]
transpose=[]
for i in range(len(l1[0])):
    row=[]
    for j in range(len(l1)):
        row.append(l1[j][i])
    transpose.append(row)
print(transpose)
# print("hello wolrd")
