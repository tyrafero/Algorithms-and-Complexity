import random


# print(unsort)
# sort1= []
# sort1= sorted(unsort)
# print(sort1)

def insertion_list(arr):
    for i in range(1,len(arr)):
        value= arr[i]
        j=i-1
        while j>=0 and value<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=value
    return arr

unsort= [random.randint(1,50) for i in range(50)]
print(unsort)
insertion_list(unsort)
print(unsort)
