a=int(input())
count=0
b=input()
for i in range(len(b)-1,-1,-1):
    print(a*int(b[i]))

count+=a*int(b[2])
count+=a*int(b[1])*10
count+=a*int(b[0])*100
    
print(count)