
def removeDuplicates(nums) -> int:
    arr = []
    i = 0
    while i < len(nums) - 1:
        if nums[i] not in arr:
            arr.append(i)
            print(arr)
            i += 1
        else:
            del nums[i]
    print(nums)
    # return len(nums)

removeDuplicates([1,1,2])