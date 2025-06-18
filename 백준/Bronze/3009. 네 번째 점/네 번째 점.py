matrix=[]
li2=[]
li3=[]
for i in range(3):
    li=list(map(int,input().split()))
    matrix.append(li)
    
for i in matrix:
    li2.append(i[0])
    
for i in matrix:
    li3.append(i[1])
    

    
for i in li2:
    if li2.count(i)==1:
        print(i,end=" ")
        
for i in li3:
    if li3.count(i)==1:
        print(i,end=" ")
    
    