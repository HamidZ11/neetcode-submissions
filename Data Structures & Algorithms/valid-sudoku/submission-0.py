class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            new_set = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in new_set:
                    return False
                else:
                    new_set.add(val)

        for col in range(9):
            new_set = set()
            for row in range(9):
                val = board[row][col]
                if val ==".":
                    continue
                if val in new_set:
                    return False
                else: 
                    new_set.add(val)

        boxes = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box = (row // 3, col // 3)

                if box not in boxes:
                    boxes[box] = set()
                if val in boxes[box]:
                    return False
                else: 
                    boxes[box].add(val)
        return True

