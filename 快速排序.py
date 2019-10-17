def q_sort(l1):
    if len(l1)<=1:
        return l1
    pivot = l1[0]
    left_list, right_list = [], []
    for le in l1[1:]:
        if le<pivot:
            left_list.append(le)
        else:
            right_list.append(le)
    return q_sort(left_list) + [pivot] + q_sort(right_list) 
n = int(input())
nums = [int(x) for x in input().split()]
nums = q_sort(nums)
print(nums)