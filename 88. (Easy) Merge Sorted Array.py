nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
# -> nums1 = [1,2,2,3,4]

p = 0
for i in range(len(nums1) - len(nums2), len(nums1)):
    nums1[i] = nums2[p]
    p += 1
nums1 = sorted(nums1)
print(nums1)