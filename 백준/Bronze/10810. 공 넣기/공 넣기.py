m,n=map(int,input().split())
li=[0 for i in range(m)]
for i in range(n):
    li2=list(map(int,input().split()))
    for i in range(li2[0]-1,li2[1]):
        li[i]=li2[2]

for i in li:
    print(i,end=' ')