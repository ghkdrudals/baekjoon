n,m=map(int,input().split())
li=[i for i in range(1,n+1)]
for i in range(m):
    li2=[]
    a,b=map(int,input().split())
    for i in range(a-1,b):
        li2.append(li[i])
    
    for i in range(a-1,b):
        del li[a-1]
    for i in li2:
        li.insert(a-1,i)

for i in li:
    print(i,end=" ")

