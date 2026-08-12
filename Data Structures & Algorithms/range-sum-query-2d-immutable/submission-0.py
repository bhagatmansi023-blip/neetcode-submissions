class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # Create prefix sum matrix
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build prefix sum matrix
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):

                self.prefix[r][c] = (
                    matrix[r - 1][c - 1]
                    + self.prefix[r - 1][c]
                    + self.prefix[r][c - 1]
                    - self.prefix[r - 1][c - 1]
                )

    def sumRegion(self, row1, col1, row2, col2):

        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )