from typing import Optional

from Problem import ProblemClass


class Problem2(ProblemClass):
    @classmethod
    def read_input(cls, inp: str) -> tuple[list[int], list[int]]:
        reports = inp.splitlines()
        reports_split = [l.split(" ") for l in reports]
        return [[int(l) for l in r] for r in reports_split]

    @classmethod
    def compare_numbers(cls, num1: int, num2: int, direction: bool) -> bool:
        if direction and 1 <= num2 - num1 <= 3:
            return True
        if not direction and 1 <= num1 - num2 <= 3:
            return True
        return False

    @classmethod
    def determine_direction(cls, level: list[int]) -> Optional[bool]:
        first = level[0]
        second = level[1]
        if first == second:
            return None
        return second > first

    @classmethod
    def is_level_safe(cls, level: list[int]) -> bool:
        direction = Problem2.determine_direction(level)
        if direction is None:
            return False
        for i, l in enumerate(level):
            if i == len(level) - 1:
                break
            if not Problem2.compare_numbers(level[i], level[i + 1], direction):
                return False

        return True

    @classmethod
    def is_level_safe_with_modifications(cls, level: list[int]):
        if Problem2.is_level_safe(level):
            return True
        idx = 0
        while True:
            level_modified = level.copy()
            del level_modified[idx]
            if Problem2.is_level_safe(level_modified):
                return True
            idx += 1
            if idx == len(level_modified) + 1:
                break

        return False

    def _solve_p1(self, inp: str) -> str:
        levels = Problem2.read_input(inp)
        return str(sum([int(Problem2.is_level_safe(level)) for level in levels]))

    def _solve(self, inp: str) -> str:
        levels = Problem2.read_input(inp)
        return str(sum([int(Problem2.is_level_safe_with_modifications(level)) for level in levels]))
