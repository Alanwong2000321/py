
def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
 
n = int(input())
nums = [int(x) for x in input().split()]
nums = bubble_sort(nums)
print(*nums)


print()