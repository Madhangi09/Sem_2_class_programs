num=int(input("Enter the no on elements : "))
arr=[]
for i in range(num):
    x=int(input("Enter the number : "))
    arr.append(x)
non_zero=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[non_zero],arr[i]=arr[i],arr[non_zero]
        non_zero+=1
print("Updated array : ",arr)
