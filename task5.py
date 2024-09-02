# Task 5: Write a program that takes a list of numbers and finds the subarray with the maximum sum (Kadane's Algorithm).
def find_max_subarray(nums):
    if not nums:
        return 0,[]
# initialize variables
    max_ending_here=nums[0]
    max_so_far = nums[0]
    start =0
    end=0
    s=0
    for i in range(1,len(nums)):
        if nums[i] >max_ending_here + nums[i]:
            max_ending_here=nums[i]
            s=i
        else:
            max_ending_here+= nums[i]
# update max_so_far and the indexes of a new maximum is found
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i
    return max_so_far, nums[start:end+1]

nums=[-2,1,-3,4,-1,2,1,-5,4]
max_sum,subarray=find_max_subarray(nums)
print(f"MAXIMUM SUM : {max_sum}")
print(f"SUBARRAY WITH MAXIMUM SUM : {subarray}")