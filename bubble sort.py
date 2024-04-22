def performbubblesort(nums):
    n=len(nums)

    for fixthisindex in range(n -1,0,n):
        for index in range(fixthisindex):
            if nuuums[index]>nums[index+1]:
                temp=nums[index]
                nums=[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
nums=[15,10,8,20,25,18,22,21]
print("before sorting:")
print(nums)
performbubblesort(nums)
print("after sorting:")
print(nums)  




