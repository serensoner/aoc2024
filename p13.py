import re
from typing import Optional
from ortools.linear_solver import pywraplp
from ortools.math_opt.python.solve import solve

from Problem import ProblemClass




def solve_using_ortools(
        a_incr: tuple[int, int],
        b_incr: tuple[int, int],
        prize: tuple[int, int],
) -> Optional[tuple[int, int]]:
    solver = pywraplp.Solver.CreateSolver('SCIP')
    a = solver.IntVar(0, solver.infinity(), 'a')
    b = solver.IntVar(0, solver.infinity(), 'b')

    solver.Minimize(3 * a + b)

    for i in range(2):
        solver.Add(a * a_incr[i] + b * b_incr[i] == prize[i])

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return solver.Objective().Value()


class Problem13(ProblemClass):
    def read_input(self, inp: str) -> list[dict[str, tuple[int, int]]]:
        lines = inp.splitlines()
        numlines = len(lines)
        ret = []
        for i in range(numlines // 4 + 1):
            nums = re.findall(r"X[+=](\d+), Y[+=](\d+)", "".join(lines[i*4:i*4+3]))
            ret.append({
                "a_incr": tuple(int(c) for c in nums[0]),
                "b_incr": tuple(int(c) for c in nums[1]),
                "prize": tuple(int(c) for c in nums[2])
            })
        return ret

    def _solve_p1(self, inp: str) -> int:
        prizes = self.read_input(inp)
        total_cost = 0
        for prize in prizes:
            found = solve_using_ortools(**prize)
            if found:
                total_cost += found

        return str(int(total_cost))


    def _solve(self, inp: str) -> str:
        prizes = self.read_input(inp)
        for p in prizes:
            pp = p["prize"]
            p["prize"] = (10**13 + pp[0], 10**13 + pp[1])

        total_cost = 0
        for prize in prizes:
            found = solve_using_ortools(**prize)
            if found:
                total_cost += found

        return str(int(total_cost))
