l1=[[1,2,3],[4,5,6]]
print("Original Matrix:", l1) # Ee line add chey
transpose=[]
for i in range(len(l1[0])):
    row=[]
    for j in range(len(l1)):
        row.append(l1[j][i])
    transpose.append(row)
print("Transposed Matrix:", transpose)