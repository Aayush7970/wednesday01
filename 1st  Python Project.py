#!/usr/bin/env python
# coding: utf-8

# In[ ]:



        


# In[16]:


name=input('Name Please! : ')
print('Hello',name,"My name is 3A's alexa")
if name[0]=='A' or name[0]=='a':
    print('💥⭕ You are so deremined , having so much patient , open minded and Practical person 😁')
if name[0]=='R' or name[0]=='r':
      print('💥⭕ You are so virtuous, powerful, pleasant and child lover 😊')
print("What do you want's from me ? ")
print(''' 
          1. Reverse the word :
          2. Check palindrome :
          3. Check the prime no. :
          4. Factorial of the number :
          5. Average of a no. :
          6. Sum of the no. :
          7. Substraction of the no. :
          8. Intresting facts :''')

n=int(input('Enter the number as shown above ☝️: '))

if n==1:
    str1=input("Give me a word for reversing : ")
    print(str1[ : :-1])
    
    
if n==2:
    str2=input('Give me a word : ')
    if str2[ : :-1]==str2:
        print('Yes , The given word is having Palindrome ✌️')
    else :
        print('Nope , The given word is not in Palindrome 🤷‍♂️')
        
        
if n==3:
    n1=int(input('Give me a number for checking Prime : '))
    a=True
    for i in range(2,n1):
        if n1%i==0:
            a=False
    if a:
        print('Yes , The given no. is prime ✌️')
    else :
        print('No , The given no. is not prime 🤷‍♂️')
        
        
if n==4:
    n2=int(input('No. for factorial : '))
    f=1
    for i in range(1,n2+1):
        f=f*i
    print(f)
    
    
if n==5:
    print(" 👉👉 Enter all the numbers using a single space ")
    n1=input().split()
    a=[]
    avr=0
    len_n1=len(n1)
    for i in n1:
        x=int(i)
        a.append(x)
    for j in a:
        avr=avr+j
    print('Average of the given no. is : ', avr//len_n1)

    
if n==6:
    print("👉👉 do sum using using '+' sign , eg.= 2+3+5 and it will answer 8")
    n1=input().split('+')
    a=[]
    sum=0
    for i in n1:
        a.append(int(i))
    for j in a:
        sum=sum+j
    print('Sum of the given no. is : ',sum)
    
    
if n==7:
    print("👉👉 do substraction using using '-' sign , eg.= 5-2-3 and it will answer 0")
    n1=input().split('-')
    a=[]
    g=n1[0]
    sub=int(g)
    for i in n1:
        a.append(int(i))
    for j in a[1:]:
        sub=sub-j
    print('Substraction of the given no. is : ',sub)
        
        
if n==8:
    print('''
                1. A snail can sleep for three years.😮.
                2. Almonds are a member of peach family 🤔 . 
                3. Elephants are the only animals that can’t jump 😮.
                4. Coca-Cola was originally green because of fresh cocoa leaves 😮.
                5. Like fingerprints , everyone's tongue print is different 🤔.''')
        


# In[ ]:




