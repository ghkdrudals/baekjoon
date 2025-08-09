n=int(input())
count1=0
count2=0
if n%4==0:
	count1+=1
if n%100!=0:
	count2+=1
if n%400==0:
	count2+=1

if count1==1 and count2>=1:
	print(1)
else:
	print(0)