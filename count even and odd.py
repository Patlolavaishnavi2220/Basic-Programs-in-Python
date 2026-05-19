#To find count of even and odd numbers in list
lst=list(map(int,input().split()))
even=0
odd=0
for i in lst:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)
'''
output:
1 2 3 4
2 2
'''
