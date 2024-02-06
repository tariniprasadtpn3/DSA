# Example 1:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Result: YES (for 1st variant)
#        [1, 3] (for 2nd variant)
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

# Example 2:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
# Result: NO (for 1st variant)
# 	[-1, -1] (for 2nd variant)
# Explanation: There exist no such two numbers whose sum is equal to the target.


def twoSumProblem(N,Arr,target):
    dict = {}
    for i, num in enumerate(Arr):
        diff = target - num
        if diff in dict:
            return dict[diff],i
        dict[num] = i
    return    


N = int(input("Enter Number Of Element Want To Store in An Array : "))

Arr = []

for i in range(N):
    element = int(input("Enter Array : "))
    Arr.append(element)

print("Array is : ",Arr)

target = int(input("Enter Target : "))

Result = twoSumProblem(N,Arr,target)

print(Result)