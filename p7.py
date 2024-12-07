from fileinput import lineno
from itertools import product

from Problem import ProblemClass


class Problem7(ProblemClass):
    def read_input(self, inp: str):
        lines = inp.splitlines()
        lines = [l.split(":") for l in lines]
        return [{
            "soln": int(l[0]),
            "numbers": [int(a) for a in l[1].split()]
        } for l in lines]

    def calc_line(self, soln: int, numbers: list[int], operations: list[str]):
        operation_combinations = list(product(operations, repeat=len(numbers) - 1))
        for op_comb in operation_combinations:
            op_comb = list(op_comb)

            def weird_precedence_eval(soln_: int, ops: list[str]):
                result = numbers[0]
                for i in range(len(ops)):
                    if result > soln_:
                        return None
                    if ops[i] == "*":
                        result = result * numbers[i + 1]
                    if ops[i] == "+":
                        result = result + numbers[i + 1]
                    if ops[i] == "||":
                        result = int(str(result) + str(numbers[i + 1]))


                return result

            try:
                result = weird_precedence_eval(soln_=soln, ops=op_comb)
                if result == soln:
                    return True
            except:
                pass

        return False

    def _solve_p1(self, inp: str) -> str:
        lines = self.read_input(inp)
        calibration = sum([
            l["soln"] for l in lines
            if self.calc_line(l["soln"], l["numbers"], operations=["*", "+"])
        ])

        return str(calibration)

    def _solve(self, inp: str) -> str:
        lines = self.read_input(inp)
        calibration = sum([
            l["soln"] for l in lines
            if self.calc_line(l["soln"], l["numbers"], operations=["*", "+", "||"])
        ])

        return str(calibration)
