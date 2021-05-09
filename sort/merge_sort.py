def merge_array(nums1: list, nums2: list):
    merged = []
    while nums1 != [] or nums2 != []:
        if nums1 == []:
            for i in range(len(nums2)):
                merged.append(nums2[i])
            break
        if nums2 == []:
            for i in range(len(nums1)):
                merged.append(nums1[i])
            break
        if nums1[0] < nums2[0]:
            merged.append(nums1.pop(0))
        elif nums1[0] > nums2[0]:
            merged.append(nums2.pop(0))
    return merged

def merge_sort(nums: list):
    if len(nums) <= 1: return nums
    if len(nums) == 2: 
        if nums[0] > nums[1]:
            nums[1], nums[0] = nums[0], nums[1]
        return nums
    else:
        mid = len(nums) // 2
        left = nums[0:mid]
        right = nums[mid:]
        return merge_array(merge_sort(left), merge_sort(right))


array = [6, 3, 9, 1, 5, 7, 2, 8, 4] 
result = merge_sort(array) 
print(result)