#To Reverse the elements in the list
lst=list(map(int,input().split()))
n=len(lst)
for i in range(n//2):
    lst[i],lst[n-i-1]=lst[n-i-1],lst[i]
print(lst)
'''
output:
1 8 6 3
[3, 6, 8, 1]
'''
