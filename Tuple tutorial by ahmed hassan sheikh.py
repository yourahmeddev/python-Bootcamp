#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Method to create Tuple
tup1=(1,"Ahmed",True,3.14,5+4j)


# In[2]:


print(tup1)


# In[4]:


#How to check data type of Tuple
print(type(tup1))


# In[5]:


#Extracting the indiviual values
print(tup1[0])


# In[6]:


#Extracting the last value from tuple data structure
print(tup1[-1])


# In[7]:


#Extracting the values from tuple in form of sequence
print(tup1[0:3])


# In[10]:


#Basic Funtions on Tuple
#How to find the length of tuple
print(len(tup1))


# In[11]:


#How to concatinate two tuples
tup1=(1,2,3,4)
tup2=(5,6,7,8)
print(tup1+tup2)


# In[13]:


#Repeating the elements of tuple
print(tup1*3)


# In[14]:


#repeating the elements of tuple and conactination alongside
tup1=(1,2,3)
tup2=(4,5,6)
print(tup1*2+tup2)


# In[15]:


#Finding the minimum value from tuple
tup1=(1,2,3,4,5,6,7,8)
print(min(tup1))


# In[16]:


#Finding the maximum values from tuple
print(max(tup1))

