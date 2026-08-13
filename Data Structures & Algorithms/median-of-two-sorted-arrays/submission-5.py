class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        A = nums1
        B = nums2
        m, n = len(A), len(B)

        left_size = (m + n + 1) // 2
        left = 0
        right = len(A)

        while left <= right:
            i = (left+right) // 2
            j = left_size - i 
            A_left = A[i-1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")

            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            # Correct partition
            if A_left <= B_right and B_left <= A_right:
                # Odd total length
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))

                # Even total length
                left_max = max(A_left, B_left)
                right_min = min(A_right, B_right)

                return (left_max + right_min) / 2
            # Too many elements taken from A
            elif A_left > B_right:
                right = i - 1

            # Too few elements taken from A
            else:
                left = i + 1