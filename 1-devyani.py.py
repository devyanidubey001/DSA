#!/usr/bin/env python
# coding: utf-8

# In[5]:


#INSERTION_SORT
def InsertionSort(arr):
 for j in range(1,len(arr)):
    #setting key as the second element of the array in the first iteration and then moving forward
    key=arr[j]
    i=j-1
    #moving the elements to next index while key is smaller than the current element.
    while i >=0 and arr[i] > key:
            arr[i+1]=arr[i]
            i=i-1
    arr[i+1]=key

arr=[2,1,3,7,8,90,29]
InsertionSort(arr)
print(arr)


#MERGE_SORT

def merge(A,p,q,r):
    n1 = q-p+1
    n2=r-q
    # create left and right two arrays
    L = [0] * (n1)
    R = [0] * (n2)
    
    #taking element from L and R
    for i in range(0, n1):
        L[i] = A[p + i]
 
    for j in range(0, n2):
        R[j] = A[q + 1 + j]
    # Merging the arrays
    i=0
    j=0
    k=p
    
    #copying from the array that is left with elements after sorting
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(A, p, r):
    if p < r:
          q = p+(r-p)//2
          mergeSort(A, p, q)
          mergeSort(A, q+1, r)
          merge(A, p, q, r)
 
A= [12, 11, 13, 5, 6, 7]
n=len(A)
mergeSort(A,0,n-1)
print(A)


# In[ ]:





# In[ ]:





# In[ ]:




