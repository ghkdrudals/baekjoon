n=int(input())
li2=[]
li3=[]
matrix=[]
cols=0
rows=0
for i in range(n):
    li=list(map(int,input().split()))
    matrix.append(li)
    
for i in matrix:
    li2.append(i[0])
    li3.append(i[1])
    
li2.sort(reverse=True)
cols=li2[0]-li2[n-1]
li3.sort(reverse=True)
rows=li3[0]-li3[n-1]

print(cols*rows)
    
    
    
    