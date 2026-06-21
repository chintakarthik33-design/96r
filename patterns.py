n=3
m=5
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()


n=3
m=5
for i in range(n):
    for j in range(m):
        print("1",end=" ")
    print()

n=3
for i in range(n):
    for j in range(n):
        print(i,j,end=" ")
    print()


n=3
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()


n=3
val=1
for i in range(n):
    for j in range(n):
        print(val,end=" ")
        val+=1
    print()

n=3
val=65
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
    print()


n=3
for i in range(n):
    val=65
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
    print()









