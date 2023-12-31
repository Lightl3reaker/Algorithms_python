#making a binary search using recursion
def binsearch(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) //2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binsearch(data,target,low,mid-1)
        else:
            return binsearch(data,target,mid+1,high)

inputs=[int(x) for x in input("Enter data sequence:").split()]
finditem=int(input("Enter data to find:"))
inputs.sort()
print(inputs)
result=binsearch(inputs,finditem,0,len(inputs)-1)
if result is not False:
    print(f"Found item in index {result}")
else:
    print("Not Found")
