from collections import deque
from typing import Optional

from Problem import ProblemClass


class Problem22(ProblemClass):
    sequences: dict[tuple[int, int, int, int], int]

    def read_input(self, inp: str) -> list[int]:
        self.sequences = {}
        return [int(l) for l in inp.splitlines()]

    def mix(self, secret: int, new_secret: int) -> int:
        return  new_secret ^ secret

    def prune(self, secret: int) -> int:
        return secret % 16777216

    def solve_secret(self, secret: int) -> int:
        secret = self.prune(self.mix(secret, secret * 64))
        secret = self.prune(self.mix(secret, secret // 32))
        secret = self.prune(self.mix(secret, secret * 2048))
        return secret

    def solve_secret_n_times(self, secret: int, times: int):
        for n in range(times):
            secret = self.solve_secret(secret)

        return secret

    def solve_secret_n_times_p2(self, secret: int, times: int):
        stack = deque(maxlen=4)
        local: dict[tuple[int, int, int, int], int] = {}
        for n in range(4):
            next_secret = self.solve_secret(secret)
            diff = next_secret % 10 - secret % 10
            stack.append(diff)
            secret = next_secret

        for n in range(times - 4):
            next_secret = self.solve_secret(secret)
            diff = next_secret % 10 - secret % 10
            stack.append(diff)
            secret = next_secret

            stack_tuple: tuple[int, int, int, int] = tuple(stack)
            if stack_tuple not in local:
                local[stack_tuple] = next_secret % 10

        return local

    def _solve_p1(self, inp: str) -> str:
        secrets = self.read_input(inp)
        output = {}
        for secret in secrets:
            output[secret] = self.solve_secret_n_times(secret, 2000)

        return str(sum(output.values()))

    def _solve(self, inp: str) -> str:
        secrets = self.read_input(inp)
        for secret in secrets:
            local = self.solve_secret_n_times_p2(secret, 2000)
            for k, v in local.items():
                if k in self.sequences:
                    self.sequences[k] += v
                    continue
                self.sequences[k] = v

        return str(max(self.sequences.values()))
