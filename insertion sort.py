def performInsertionSort(nums):
    n = len(nums)
    # [12, 3, 10, 18, 9, 200, 167]
    # n = 5
    # 1 2 3 4
    for index in range(1, n):
        temp = nums[index]
        position = index - 1 
        while position >= 0 and nums[position] > temp:
            nums[position + 1] = nums[position]
            position -= 1 
 
        nums[position + 1] = temp 
        print(nums) 
nums = list(map(int,input().split()))
 
print("Before sorting:")
print(nums)
performInsertionSort(nums)
 
print("After sorting:")
print(nums)
