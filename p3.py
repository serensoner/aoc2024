import re
from Problem import ProblemClass


class Problem3(ProblemClass):
    @classmethod
    def read_input(cls, inp: str) -> tuple[list[int], list[int]]:
        return len(inp)

    def _solve_p1(self, inp: str) -> str:
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, inp)
        parsed_values = [(int(x), int(y)) for x, y in matches]
        return str(sum([p[0] * p[1] for p in parsed_values]))

    def _solve(self, inp: str) -> str:
        inp = ''.join(inp)
        pattern = r"don't\(\).*?do\(\)"
        filtered_string = re.sub(pattern, "", inp)
        return self._solve_p1(filtered_string)
