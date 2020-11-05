class Solution(object):
    def merge(self, nums1, m, nums2, n):

        # Method 1:
        index = 0
        for i in range(n):
            if nums2[i] > nums1[m+i-1]:
                nums1[m+i] = nums2[i]
            elif nums2[i] <= nums1[0]:
                for h in range(m+i, 0, -1):
                    nums1[h] = nums1[h-1]
                nums1[0] = nums2[i]
                index += 1
            else:
                print(nums2[i], index)
                j = index
                while j < m+i:
                    print(nums2[i], nums1[j], i, j)
                    if nums2[i] <= nums1[j]:
                        for k in range(m+i, j, -1):
                            nums1[k] = nums1[k-1]
                        nums1[j] = nums2[i]
                        index = j+1
                        j = m+i+1
                    else:
                        j += 1
                    print(nums1)
        return nums1

        # Method 2:
        p1 = m - 1
        p2 = n - 1
        p = m + n + 1
        nums = []
        while p1 > 0 and p2 > 0:
            if nums1[p1] < nums2[p2]:
                nums[p] = nums2[p2]
                p2 -= 1
            else:
                nums[p] = nums1[p1]
                p1 -= 1
            p -= 1
        return nums

        # Method 2:
        # arr= []
        #
        # index=0
        # for i in range(m):
        #     if index < n and nums1[i] < nums2[index]:
        #         arr.append(nums1[i])
        #     else:
        #         while index < n and nums2[index] < nums1[i]:
        #             arr.append(nums2[index])
        #             index += 1
        #         arr.append(nums1[i])
        #
        # for i in range(index,n):
        #     arr.append(nums2[i])
        # for j in range(len(arr)):
        #     nums1[j] = arr[j]
        # return nums1


s = Solution()
A = [-7, -6, -5, -4, 0, 0, 0, 0]
B = [-10, -10, -8, -6]
m = 4
n = 4
print(s.merge(A, m, B, n))
