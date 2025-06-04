nums =[3,2,2,3]
val = 3

def remove_element(nums: list, val : int) ->int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val :
            nums[k] = nums[i]
            k+=1
    return k
x = remove_element(nums = nums , val=val)
print(x)
# print(nums[:x])

