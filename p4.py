import re
from Problem import ProblemClass


class Problem4(ProblemClass):
    @classmethod
    def read_input(cls, inp: str) -> list[str]:
        return inp.splitlines()

    def search(self, lines, i, j, search_dir_x: int, search_dir_y: int):
        word = "XMAS"
        numlines = len(lines)
        linelen = len(lines[0])

        try:
            for cntr in range(4):
                pi = i + search_dir_x * cntr
                pj = j + search_dir_y * cntr
                if not (0 <= pi < numlines):
                    return False
                if not (0 <= pj < linelen):
                    return False
                if lines[pi][pj] != word[cntr]:
                    return False

            return True
        except:
            return False

    def search_p2(self, lines, i, j, search_dir_y: int):
        numlines = len(lines)
        linelen = len(lines[0])
        try:
            prev_i = i - 1
            prev_j = j - search_dir_y
            next_i = i + 1
            next_j = j + search_dir_y
            if not (0 <= prev_i < numlines) or not (0 <= next_i < numlines):
                return False
            if not (0 <= prev_j < linelen) or not (0 <= next_j < linelen):
                return False
            # print(f"{(prev_i, prev_j)}, {(i, j)} {(next_i, next_j)}")
            chars = (lines[prev_i][prev_j], lines[next_i][next_j])
            if chars not in [("M", "S"), ("S", "M")]:
                return False

            return True
        except:
            return False


    def _solve_p1(self, inp: str) -> str:
        lines = Problem4.read_input(inp)
        found = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] != "X":
                    continue
                for search_dir in [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if self.search(lines, i, j, search_dir[0], search_dir[1]):
                        found += 1

        return str(found)

    def _solve(self, inp: str) -> str:
        lines = Problem4.read_input(inp)
        found = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] != "A":
                    continue
                if self.search_p2(lines, i, j, 1) and \
                    self.search_p2(lines, i, j, -1):
                    found += 1

        return str(found)

