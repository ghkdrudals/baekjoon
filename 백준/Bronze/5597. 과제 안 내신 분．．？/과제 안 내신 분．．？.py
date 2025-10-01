li=[i for i in range(1,30+1)]
li2=[]
for i in range(28):
    n=int(input())
    li2.append(n)

for i in li2:
    if i in li:
        li.remove(i)

for i in li:
    print(i)