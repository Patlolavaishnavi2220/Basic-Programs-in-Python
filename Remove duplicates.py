#To Remove duplicates from the given list
#This code works only on sorted list
lst=list(map(int,input().split()))
i=0
n=len(lst)
for j in range(1,n):
    if(lst[i]!=lst[j]):
        lst[i+1]=lst[j]
        i+=1
print(lst[0:i+1])
'''
output:
1 1 2 2 3 4
[1, 2, 3, 4]
'''
