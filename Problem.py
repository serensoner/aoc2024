from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class ProblemClass:
    @abstractmethod
    def _solve(self, inp: str) -> str:
        pass

    def _solve_p1(self, inp: str) -> int:
        return self._solve(inp)

    def solve(self, part: str) -> int:
        with open(f'inputs/{self.__class__.__name__}_input.txt') as f:
            inp = f.read()

        solve_func = self._solve_p1 if part == '1' else self._solve
        solution = solve_func(inp)
        print(f'Solution to part {part} is {solution}')

    def test(self, part: str):
        print(f'Testing part {part}')
        with open(f'inputs/{self.__class__.__name__}_sample_input_part{part}.txt') as f:
            inp = f.read()

        solve_func = self._solve_p1 if part == '1' else self._solve

        solution = str(solve_func(inp))

        with open(f'inputs/{self.__class__.__name__}_sample_output_part{part}.txt') as f:
            output = f.read()

        print(f'Test solution was {output}, my soln {solution}')
        assert solution == output