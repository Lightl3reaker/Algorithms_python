#Insertion sort
##it has two parts (1)Sorted part and (2)Unsorted part
#generally first element of array is sorted part and others unsorted.
#then  sort latter part by iterating each element.
#Complexity of O(n^2)
def insertsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

my_array=[12,11,13,6,5]
insertsort(my_array)
print(my_array)
