
# 처음 생각

# def searchMatrix(self, matrix, target):
#         for i in matrix:
#             if target in i:
#                 return True
#         return False

# 이진 탐색
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

# 배열 첫번째, 마지막
row, col = 0, len(matrix[0]) - 1

while row < len(matrix):
        # 배열에 target이 있으면 True
        if matrix[row][col] == target :
                print('True')
                break
        # 배열 값이 Target 보다 크면 왼쪽으로 
        elif matrix[row][col] > target:
                col = col - 1
        # 아니면 아래로
        else:
                row = row + 1

# 리트코드 용
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col > -1:
            if matrix[row][col] == target :
                return True
            elif matrix[row][col] > target:
                col = col - 1
            else:
                row = row + 1

        return False


