class Solution:
    def sort012(self, arr):
        # 0 1 2 0 1 2 

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]