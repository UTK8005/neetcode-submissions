
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Validate rows
        for i in board:
            for j in i:
                if j == ".":
                    continue
                if i.count(j) > 1:
                    return False

        # Validate columns
        for i in range(len(board)):
            column_aggregate = []

            for j in range(len(board)):
                if board[j][i] == ".":
                    continue

                if board[j][i] in column_aggregate:
                    return False

                column_aggregate.append(board[j][i])

        # Validate 3x3 grids
        for i in range(0, len(board)-2, 3):
            for j in range(0, len(board)-2, 3):
                window = []

                for s in range(i, i+3):
                    for k in range(j, j+3):

                        if board[s][k] == ".":
                            continue

                        if board[s][k] in window:
                            return False

                        window.append(board[s][k])

        return True
