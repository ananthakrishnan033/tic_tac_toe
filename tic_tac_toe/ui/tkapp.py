import tkinter as tk
from tkinter import messagebox
from ..game import Game
from ..player import Player

class TkApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.players = [Player("Player X", "X"), Player("Player O", "O")]
        self.game = Game(self.players)
        self.game.start()
        self.buttons = []
        self.scores = {self.players[0].mark: 0, self.players[1].mark: 0}
        top = tk.Frame(self.root)
        top.pack(pady=8)
        self.status = tk.Label(top, text="Turn: " + self.game.current_player().name, font=("Segoe UI", 12))
        self.status.pack(side="left", padx=8)
        self.restart_btn = tk.Button(top, text="Restart", command=self.restart, state="disabled")
        self.restart_btn.pack(side="right", padx=8)
        score_frame = tk.Frame(self.root)
        score_frame.pack()
        self.score_labels = {}
        for p in self.players:
            lbl = tk.Label(score_frame, text=p.name + ": 0", font=("Segoe UI", 12))
            lbl.pack(side="left", padx=12)
            self.score_labels[p.mark] = lbl
        grid = tk.Frame(self.root)
        grid.pack(padx=10, pady=10)
        for r in range(3):
            row = []
            for c in range(3):
                btn = tk.Button(grid, text=" ", width=6, height=3, font=("Segoe UI", 18), bg="#f0f0f0", activebackground="#e0e0e0")
                btn.grid(row=r, column=c, padx=4, pady=4)
                btn.configure(command=lambda rr=r, cc=c: self.on_click(rr, cc))
                row.append(btn)
            self.buttons.append(row)

    def pulse(self, btn, times=4):
        def step(i):
            if i >= times:
                btn.configure(bg="#f0f0f0")
                return
            btn.configure(bg="#ffd54f" if i % 2 == 0 else "#f0f0f0")
            self.root.after(120, lambda: step(i + 1))
        step(0)

    def on_click(self, r, c):
        status = self.game.make_move(r, c)
        if status == "invalid":
            self.status.configure(text="Cell occupied")
            return
        mark = self.game.board.grid[r][c]
        self.buttons[r][c].configure(text=mark)
        self.pulse(self.buttons[r][c])
        if status == "win":
            line = self.game.board.winning_line()
            if line:
                for rr, cc in line:
                    self.buttons[rr][cc].configure(bg="#81c784")
            winner = None
            wmark = self.game.board.winner()
            for p in self.players:
                if p.mark == wmark:
                    winner = p
                    break
            self.status.configure(text="Winner: " + winner.name)
            self.scores[winner.mark] += 1
            self.update_scores()
            for r0 in range(3):
                for c0 in range(3):
                    self.buttons[r0][c0].configure(state="disabled")
            self.restart_btn.configure(state="normal")
            messagebox.showinfo("Game Over", "Winner: " + winner.name)
            return
        if status == "draw":
            self.status.configure(text="Draw")
            for r0 in range(3):
                for c0 in range(3):
                    self.buttons[r0][c0].configure(state="disabled")
            self.restart_btn.configure(state="normal")
            messagebox.showinfo("Game Over", "Draw")
            return
        self.status.configure(text="Turn: " + self.game.current_player().name)

    def update_scores(self):
        for mark, lbl in self.score_labels.items():
            lbl.configure(text=(self.players[0].name if mark == self.players[0].mark else self.players[1].name) + ": " + str(self.scores[mark]))

    def restart(self):
        self.game.start()
        for r in range(3):
            for c in range(3):
                btn = self.buttons[r][c]
                btn.configure(text=" ", state="normal", bg="#f0f0f0")
        self.status.configure(text="Turn: " + self.game.current_player().name)
        self.restart_btn.configure(state="disabled")

    def run(self):
        self.root.mainloop()
