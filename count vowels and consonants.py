#To find count of vowels and consonants 
s=input()
vowel = "aeiouAEIOU"
v=0
c=0
for i in s:
    if(i in vowel):
        v+=1
    else:
        c+=1
print(v,c)
'''
output:
GitHub
2 4
'''
