import sys

def maxSubArray(N,arr):
    maxi = -sys.maxsize-1
    sum =0

    for i in range(N):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi


N = int(input("Enter number of elements to be stored in an array : "))
arr = []
for i in range(N):
    elem = int(input("Enter Array : "))
    arr.append(elem)

print("Array is : ",arr)

result = maxSubArray(N,arr)
print("Result is ",result)