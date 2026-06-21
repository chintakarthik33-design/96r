l1=[[1,2,3],[4,5,6]]
transpose=[]
for i in range(len(l1[0])):
    row=[]
    for j in range(len(l1)):
        row.append(l1[j][i])
    transpose.append(row)
print(transpose)