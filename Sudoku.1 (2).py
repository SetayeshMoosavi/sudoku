fwf = "HardBoard_Project01.txt"
class Sudoku:
    def __init__(self):
        self.board = []

    def reader(self, f):
        ff = open(fwf, "r")
        for item in ff.readlines():
            self.board.append(item.rstrip("\n").split(","))
        ff.close()

    def show_board(self):
        myboard = []
        for line in self.board:
            for item in line:
                if Sudoku.check_board(self, self.board.index(line), line.index(item)):
                    if int(self.board[self.board.index(line)][line.index(item)])==0:
                        myboard.append(" ")
                    else:
                        myboard.append(item)
                else:
                    if int(self.board[self.board.index(line)][line.index(item)])==0:
                        myboard.append(" ")
                    else:
                        myboard.append("\033[33m"+str(item)+"\033[m")
        mytuple = tuple(myboard)
        myfile = """--------------------------------
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
|  +   +  +  +   +   +   +  +  |
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
|  +   +  +  +   +   +   +  +  |
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
---+---+---+----+----+----+---+-
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
|  +   +  +  +   +   +   +  +  |
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
|  +   +  +  +   +   +   +  +  |
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
---+---+---+----+----+----+---+-
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
|  +   +  +  +   +   +   +  +  |
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
|  +   +  +  +   +   +   +  +  |
| {}  {}  {} | {}  {}  {}  | {}  {}  {} |
-------------------------------- """

        print(myfile.format(*mytuple))

    def check_board(self, row, col):
        a = 0
        b = 0
        c = 0
        A=int(self.board[row][col])
        if A!=0:
            for i in range(9):
                if int(self.board[i][col]) == A:
                    a += 1
                if a > 1:
                    return False

            for j in range(9):
               if int(self.board[row][j]) == A:
                   b += 1
               if b > 1:
                   return False
            for f in range(3*(int(col)//3), (3*(int(col)//3))+3):
                for g in range(3*(int(row)//3), (3*(int(row)//3))+3):
                    if int(self.board[g][f]) == A:
                        c += 1
                    if c > 1:
                        return False
        return True

    def solve(self):
        cells = []
        for i in range(9):
            for j in range(9):
                if int(self.board[i][j]) == 0:
                    cells.append([i, j])

        def isfeasible2(row, col):
            if int(self.board[row][col]) != 0:
                return []
            else:
                l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for jj in range(9):
                    for h in l1:
                        if int(self.board[row][jj]) == h:
                            l1.remove(h)
                for ii in range(9):
                    for h in l1:
                        if int(self.board[ii][col]) == h:
                                l1.remove(h)

                for n in range(3 * (int(row) // 3), (3 * (int(row) // 3)) + 3):
                    for k in range(3 * (int(col) // 3), (3 * (int(col) // 3)) + 3):
                        for h in l1:
                            if int(self.board[n][k]) == h:
                                l1.remove(h)
                return l1

        def __solve(cell):
            if len(cell) == 0:
                return True
            else:
                for ind in isfeasible2(cell[0][0], cell[0][1]):
                    self.board[cell[0][0]][cell[0][1]] = str(ind)
                    if __solve(cell[1:]):
                        return True
                self.board[cell[0][0]][cell[0][1]] = "0"
                return False
        __solve(cells)


hi = Sudoku()
hi.reader(fwf)
hi.show_board()
print(hi.board)
hi.solve()
hi.show_board()
