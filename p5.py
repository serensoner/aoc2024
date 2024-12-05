import re
from typing import Optional

from Problem import ProblemClass
from p4 import Problem4


class Problem5(ProblemClass):
    order: dict[str, list[str]]
    lines: list[str]

    def read_input(self, inp: str):
        lines = inp.splitlines()
        order = {}
        for line_idx, line in enumerate(lines):
            if line == "":
                break
            parts = line.split("|")
            if parts[0] not in order:
                order[parts[0]] = []
            order[parts[0]].append(parts[1])

        self.lines = [l.split(",") for l in lines[line_idx + 1:]]
        self.order = order

    def is_line_correct(self, line) -> Optional[int]:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if self.order.get(line[j]) and line[i] in self.order.get(line[j]):
                    return None

        return line[int((len(line) - 1) / 2)]

    def correct_line(self, line) -> int:
        while True:
            no_change = True
            for i in range(len(line)):
                for j in range(i + 1, len(line)):
                    if self.order.get(line[j]) and line[i] in self.order.get(line[j]):
                        line[i], line[j] = line[j], line[i]
                        no_change = False
                        break

            if no_change:
                return line[int((len(line) - 1) / 2)]


    def _solve_p1(self, inp: str) -> str:
        self.read_input(inp)
        midpoints = [self.is_line_correct(line) for line in self.lines]
        correct_midpoints = [int(c) for c in midpoints if c]
        return str(sum(correct_midpoints))

    def _solve(self, inp: str) -> str:
        self.read_input(inp)
        corrected_lines = [
            int(self.correct_line(line)) for line in self.lines
            if not self.is_line_correct(line)
        ]
        return str(sum(corrected_lines))
