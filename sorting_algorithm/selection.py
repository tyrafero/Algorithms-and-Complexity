import random


def selection_list(arr):
    for i in range(len(arr)):  #i pointer traverse through lenght of arrar
        min=i                   #declaring minimum value position stays at ith position
        for j in range(i+1, len(arr)):  #j pointer starts right afer where i is and goes upto length of array
            if arr[min]>arr[j]:   #aghadi vako element ra thyakkai pachadi ko element ma kun thulo cha
                min=j             #j ko position lai min ma haldiney
        
        arr[i],arr[min] = arr[min],arr[i]  #arr[i] lai arr[min] ma and vice versa gareko
    
    for i in range(len(arr)):   
        return arr[i]                   #sorted array arr[i] ma bascha tyeslai return gareko

unsort= [random.randint(1,50) for i in range(50)]  #random sets of element generate gareko
print(unsort)                           
selection_list(unsort)                              #sorting function declare gareko
print(unsort)