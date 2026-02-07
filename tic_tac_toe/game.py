from .board import Board

class Game:
    def __init__(self, players, ui=None):
        self.board = Board()
        self.players = players
        self.ui = ui
        self.current = 0

    def start(self):
        self.board.reset()
        self.current = 0

    def current_player(self):
        return self.players[self.current]

    def switch(self):
        self.current = 1 - self.current

    def make_move(self, row, col):
        player = self.players[self.current]
        if not self.board.place(row, col, player.mark):
            return "invalid"
        w = self.board.winner()
        if w is not None:
            return "win"
        if self.board.full():
            return "draw"
        self.switch()
        return "ok"

    def run(self):
        self.start()
        while True:
            self.ui.show_board(self.board)
            player = self.players[self.current]
            r, c = self.ui.prompt_move(player)
            status = self.make_move(r, c)
            if status == "invalid":
                self.ui.show_message("Cell occupied")
                continue
            if status == "win":
                self.ui.show_board(self.board)
                for p in self.players:
                    if p.mark == self.board.winner():
                        self.ui.show_winner(p)
                        return
            if status == "draw":
                self.ui.show_board(self.board)
                self.ui.show_draw()
                return
