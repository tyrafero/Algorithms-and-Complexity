import math

import operator

def merge(arr,p,q,r):
    n1= q-p+1
    n2= r-q
    right,left=[],[]
    for i in range(n1):
        left.append(arr[p+i])
    for j in range(n2):
        right.append(arr[q+j+1])
    left.append(math.inf)
    right.append(math.inf)

    i=j=0

    for k in range(p,r+1):
        if left[i]<= right[j]:
            arr[k]= left[i]
            i+= 1
        else:
            arr[k]=right[j]
            j+=1

def merge_sort(arr,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

unsort= []
n= int(input("Enter number of elements :"))
for i in range(0,n):
    ele=int(input())
    unsort.append(ele)
print(unsort)
merge_sort(unsort,0,n-1)
print(unsort)
    