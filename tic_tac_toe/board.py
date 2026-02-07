class Board:
    def __init__(self):
        self.size = 3
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def reset(self):
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def place(self, row, col, mark):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        if self.grid[row][col] is not None:
            return False
        self.grid[row][col] = mark
        return True

    def winner(self):
        lines = []
        for r in range(self.size):
            lines.append(self.grid[r])
        for c in range(self.size):
            lines.append([self.grid[r][c] for r in range(self.size)])
        lines.append([self.grid[i][i] for i in range(self.size)])
        lines.append([self.grid[i][self.size - 1 - i] for i in range(self.size)])
        for line in lines:
            if line[0] is not None and line[0] == line[1] == line[2]:
                return line[0]
        return None

    def winning_line(self):
        for r in range(self.size):
            row = self.grid[r]
            if row[0] is not None and row[0] == row[1] == row[2]:
                return [(r, 0), (r, 1), (r, 2)]
        for c in range(self.size):
            col = [self.grid[r][c] for r in range(self.size)]
            if col[0] is not None and col[0] == col[1] == col[2]:
                return [(0, c), (1, c), (2, c)]
        diag = [self.grid[i][i] for i in range(self.size)]
        if diag[0] is not None and diag[0] == diag[1] == diag[2]:
            return [(0, 0), (1, 1), (2, 2)]
        anti = [self.grid[i][self.size - 1 - i] for i in range(self.size)]
        if anti[0] is not None and anti[0] == anti[1] == anti[2]:
            return [(0, 2), (1, 1), (2, 0)]
        return None

    def full(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] is None:
                    return False
        return True

    def empty_positions(self):
        pos = []
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] is None:
                    pos.append((r, c))
        return pos
