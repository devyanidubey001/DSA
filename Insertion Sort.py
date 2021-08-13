#!/usr/bin/env python
# coding: utf-8

# In[3]:


def InsertionSort(arr):
 for j in range(1,len(arr)):
    key=arr[j]
    i=j-1
    while i >=0 and arr[i] > key:
            arr[i+1]=arr[i]
            i=i-1
    arr[i+1]=key
arr=[2,1,3,7,8,90,29]
InsertionSort(arr)
print(arr)
        
        
    


# In[ ]:




