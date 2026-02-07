import sys

class ConsoleUI:
    def show_board(self, board):
        for r in range(board.size):
            row = []
            for c in range(board.size):
                cell = board.grid[r][c]
                row.append(cell if cell is not None else " ")
            line = " | ".join(row)
            print(line)
            if r < board.size - 1:
                print("-" * (board.size * 4 - 3))

    def prompt_move(self, player):
        print(player.name + " (" + player.mark + ") turn")
        while True:
            print("Enter row and column (1-3) separated by space:")
            s = sys.stdin.readline().strip()
            parts = s.split()
            if len(parts) != 2:
                print("Invalid input")
                continue
            try:
                r = int(parts[0]) - 1
                c = int(parts[1]) - 1
            except ValueError:
                print("Invalid numbers")
                continue
            if r < 0 or r > 2 or c < 0 or c > 2:
                print("Out of range")
                continue
            return r, c

    def show_message(self, text):
        print(text)

    def show_winner(self, player):
        print("Winner: " + player.name + " (" + player.mark + ")")

    def show_draw(self):
        print("Draw")
