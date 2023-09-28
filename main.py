class Solution:

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i = 0
        j = 0
        lst = []
        k = 0
        while i < len(nums1) and j < len(nums2):
            if int(nums1[i]) < int(nums2[j]):
                lst.append(nums1[i])
                i += 1
            elif int(nums1[i]) >= int(nums2[j]):
                lst.append(nums2[j])
                j += 1
        if i != len(nums1):
            lst.extend(nums1[i:])
        elif j != len(nums2):
            lst.extend(nums2[j:])
        lst_len = len(lst)
        if lst_len % 2 == 0:
            k = (lst[lst_len // 2] + lst[(lst_len // 2) - 1]) / 2
        else:
            k = lst[lst_len // 2]
        return k


    x = [1,2, 3, 4, 5]
    y = [3,4]
    print(findMedianSortedArrays(x, y))
