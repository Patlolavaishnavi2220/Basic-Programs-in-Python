# To check whether a given number is palindrome or not 
n=int(input())
original=n
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(original==rev):
    print("Palindrome")
else:
    print("Not a palindrome")
'''
output:
1001
Palindrome
'''
