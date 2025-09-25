a=int(input())
b=int(input())
hap=0
for i in range(b):
    c,d=map(int,input().split())
    hap+=c*d

if hap==a:
    print("Yes")
else:
    print("No")
