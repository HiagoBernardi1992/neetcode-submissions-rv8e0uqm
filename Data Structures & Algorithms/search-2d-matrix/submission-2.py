class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        mSize = len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target >= matrix[m][0] and target <= matrix[m][mSize] :
                return self.searchRow(matrix[m], target)
            elif target > matrix[m][mSize]:
                l = m + 1
            else:
                r = m - 1

        return False

    def searchRow(self, row: List[int], target: int) -> bool:
        l = 0
        r = len(row) - 1
        while l <= r:
            m = l + (r - l) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
