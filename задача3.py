def plus_one(nums):
    for i in range(len(nums)-1, -1,-1):
        if nums[i]<9:
            num[i]+=1
            return nums
        num[i]=0
    return [1]+[0]*len(nums)