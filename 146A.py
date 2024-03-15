n=int(input())
num=input()
l=list(num)
sum_1=0;sum_2=0;flag=0
for i in range(0,n//2):
    if l[i]=='4' or l[i]=='7':
        sum_1+=int(l[i])
    else:
        flag=1
        break
for i in range(n//2,n):
    if l[i]=='4' or l[i]=='7':
        sum_2+=int(l[i])
    else:
        flag=1
        break
if(sum_1==sum_2 and sum_1!=0 and flag==0):
    print("YES")
else:
    print("NO")
