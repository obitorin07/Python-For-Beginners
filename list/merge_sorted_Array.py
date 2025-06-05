def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    print(p1)
    print(p2)
    print(p)
    print(nums1[p])
    print(nums1[p1])
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            # print(nums1[p1] > nums2[p2])
            nums1[p] = nums1[p1]
            p1 -= 1
        else :
            nums1[p] = nums2[p2]
            p2 -=1
        p -= 1

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3 ;
print(merge(nums1, m, nums2, n))