#To find factorial of a number using recursion
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
n=int(input())
print(fact(n))
'''
output :
5   
120
'''
