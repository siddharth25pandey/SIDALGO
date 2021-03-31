# Bubble Sort- Time Complexity- O(n^2)
def bubble_sort(list):
    for i in range (len(list)-1):
        for j in range (len(list)-1):
            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j] 

# Insertion Sort- Time Complexity- O(n^2)
def insertion_sort(list):
    for i in range(1, len(list)): 
        key = list[i] 
        j = i-1
        while j >=0 and key < list[j] : 
            list[j+1] = list[j] 
            j -= 1
        list[j+1] = key 

# Insertion Sort- Time Complexity- O(n^2)
def selection_sort(list):
    for i in range(len(list)): 
        min_idx = i 
        for j in range(i+1, len(list)): 
            if list[min_idx] > list[j]: 
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

# Merge Sort- Time Complexity- O(nlog(n))
def merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
