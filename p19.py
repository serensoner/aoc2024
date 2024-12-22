from fileinput import lineno
from itertools import product
from typing import Optional

from Problem import ProblemClass


class Problem19(ProblemClass):
    cache: dict[str, int]

    def read_input(self, inp: str) -> tuple[set[str], list[str]]:
        self.cache = {}
        lines = inp.splitlines()
        towels = set([a.strip() for a in lines[0].split(',')])
        designs = lines[2:]
        return towels, designs

    def remove_towel_from_design(self, towel: str, design: str) -> Optional[str]:
        if towel not in design:
            return None
        return

    def solve_pattern(self, design: str, towels: set[str]) -> bool:
        if design == "":
            return True
        for towel in towels:
            if design.startswith(towel):
                output = self.solve_pattern(design[len(towel):], towels)
                if output:
                    return True

        return False

    def solve_pattern_p2(self, design: str, towels: set[str]) -> int:
        if design in self.cache:
            return self.cache[design]
        num_designs = 0
        if design == "":
            return 1
        for towel in towels:
            if design.startswith(towel):
                num_designs += self.solve_pattern_p2(design[len(towel):], towels)

        self.cache[design] = num_designs
        return num_designs

    def _solve_p1(self, inp: str) -> str:
        towels, patterns = self.read_input(inp)
        return str(len([
            pattern for pattern in patterns if self.solve_pattern(pattern, towels)]
        ))

    def _solve(self, inp: str) -> str:
        towels, patterns = self.read_input(inp)
        output = 0
        for pattern in patterns:
            output += self.solve_pattern_p2(pattern, towels)

        return str(output)
