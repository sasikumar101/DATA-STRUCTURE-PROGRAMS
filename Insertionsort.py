def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key   
arr=list(map(int,input("Enter the array element using space:").split()))
print("Array list:",arr)
insertion_sort(arr)
print("sorted list",arr)
