#To check the password is strong or weak
s=input()
small=0
capital=0
numbers=0
special=0
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        capital+=1
    elif(ord(i)>=97 and ord(i)<=122):
        small+=1
    elif(ord(i)>=48 and ord(i)<=57):
        numbers+=1
    else:
        special+=1
if(len(s)==0):
    print("please enter a password :")
else:
    if(len(s)>=8 and capital>0 and small>0 and special>0 and numbers>0):
        print("strong password")
    else:
        print("weak password")

'''
output:
#@ammu123.b
weak password
'''
