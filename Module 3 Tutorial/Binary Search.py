class Solution:
    def binarysearch(self, arr, k):
        # [1, 2, 3, 4, 5]
        # k = 3

        if k in arr:
            return arr.index(k)
        return -1