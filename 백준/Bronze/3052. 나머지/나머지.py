li=[]
for i in range(10):
    n=int(input())
    li.append(n)

for i in range(len(li)):
    li[i]=li[i]%42

li=set(li)
print(len(li))