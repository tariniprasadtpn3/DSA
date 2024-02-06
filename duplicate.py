def DuplicateCheck(N,arr):
    hashSet = set()
    for i in range(N):
        if arr[i] in hashSet:
            return "True"
        hashSet.add(arr[i])
    return "False"

N = int(input("Enter number of elemenets to be stored in an array : "))
arr = []
for i in range(N):
    elem = int(input("Enter Array : "))
    arr.append(elem)

print("Array is : ",arr)

result = DuplicateCheck(N,arr)

print(result)
 