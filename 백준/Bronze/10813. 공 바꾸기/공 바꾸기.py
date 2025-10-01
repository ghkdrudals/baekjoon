m,n=map(int,input().split())
li=[i for i in range(1,m+1)]
for i in range(n):
    a,b=map(int,input().split())
    put_a=li[a-1]
    put_b=li[b-1]
    li[a-1]=put_b
    li[b-1]=put_a

for i in li:
    print(i,end=' ')