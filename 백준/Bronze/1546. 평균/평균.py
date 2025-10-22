n=int(input())
li=list(map(int,input().split()))
ma=max(li)
for i in range(len(li)):
    li[i]=li[i]/ma*100

print(f"{sum(li)/len(li):.2f}")
