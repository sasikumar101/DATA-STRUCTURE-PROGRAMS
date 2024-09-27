def count(arr,digit,n):
    k=10
    count=[0]*(k)
    b=[0]*n
    for i in range(n):
        count[(arr[i]//digit)%10]=count[(arr[i]//digit)%10]+1
    for i in range(1,k):
        count[i]=count[i-1]+count[i]
    for i in range(n-1,-1,-1):
        count[(arr[i]//digit)%10]=count[(arr[i]//digit)%10]-1
        b[count[(arr[i]//digit)%10]]=arr[i]
    return b 

arr=[12,67,89,45,234,78,533,90,76,89] 
max_value=max(arr)
digit=1
n=len(arr)
while max_value/digit>0:
    arr= count(arr,digit,n)
    digit=digit*10
arr1=arr.copy()
print("Sorting Array:",arr1)


