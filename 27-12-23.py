#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def binarysearch(arr,x,low,high):
    if low>high:
            return -1
    mid=(low+high)//2
    if arr[mid]==x:
        return mid
        return binarysearch(arr,x,low,high)
    if arr[mid]>x:
        high=high-1
        return binarysearch(arr,x,low,high)
    if arr[mid]<x:
        low=low+1
        return binarysearch(arr,x,low,high)
    
    
    
arr=[1,2,1,3,1,4,5,2,1,5,6,1]
x=1
low = 0
high = 10
print(binarysearch(arr,x,low,high))


# In[ ]:


n= int(input("ENTER THE NUMBER :"))
i=0
while(n>0):
    n=n//10
    i=i+1
print(i)


# In[ ]:


#SUM OF NUMBERS
n= int(input("ENTER THE NUMBER :"))

sum=(n*(n+1))//2

print("SUM OF GIVEN NUMBERS ARE :",sum)


# In[ ]:


#COUNTING THE DIGITS
n=int(input("ENTER THE NUMBER :"))
i=0
while n>0:
    n=n//10
    i=i+1
print(i)


# In[4]:


#PALINDROME SYNDROM
def pal(n):
    rev=0
    temp=n
    
    while temp!=0:
        ld=temp%10
        rev=rev*10+ld
        temp=temp//10
    return rev==n

number=101010
print(pal(number))


# In[ ]:


#FACTORIAL

def fact(n):
    res=1
    for i in range(2,n+1):
        res=res*i
    return res

number=100
print(fact(number))


# In[ ]:


#RECURSIVE FACTORIAL

def fact(n):

    if n==0:
        return 1
    return n*(fact(n-1))

number=50
print(fact(number))


# In[1]:


#GREATEST COMMON DIVISOR

def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

a=70
b=49
print(gcd(a,b))


# In[34]:


# OPTIMISED GREATEST COMMON DIVISOR
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=49
b=70
print(gcd(a,b))


# In[40]:


#LEAST COMMON MULTIPLE
def lcm(a,b):
    res=max(a,b)
    while True:
        if res%a==0 and res%b==0:
            return res
        res=res+1

a=50
b=12
print(lcm(a,b))


# In[3]:


#EFFICIENT LCM

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)
    
a=10
b=70

print(lcm(a,b))


# In[55]:


#PRIME NUMBERS

def prime(n):
    if n==1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True

a=65

print("true")if prime(n) else print("false")


# In[ ]:





# In[ ]:




