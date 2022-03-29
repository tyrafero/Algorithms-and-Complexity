import random


def partition(arr, low,high):
    pivot=arr[high]
    i=low-1
    
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            
            arr[i],arr[j] =arr[j],arr[i]
        
    arr[i+1],arr[high] =arr[high], arr[i+1]
    
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi=partition(arr, low,high)
        quickSort(arr,low,pi-1)
        
        quickSort(arr,pi+1,high)

unsort= []
n= int(input("Enter number of elements :"))
for i in range(0,n):
    ele=int(input())
    unsort.append(ele)

print(unsort)
quickSort(unsort,0,n-1)
print(unsort)
        