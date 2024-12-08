from fileinput import lineno
from itertools import product
from typing import Optional

from Problem import ProblemClass


class Problem8(ProblemClass):
    def read_input(self, inp: str) -> dict:
        ret = {}
        for i, line in enumerate(inp.splitlines()):
            for j, char in enumerate(line):
                if char != ".":
                    ret.setdefault(char, []).append((i, j))
        return {
            "locs": ret,
            "y": len(inp.splitlines()),
            "x": len(inp.splitlines()[0])
        }

    @staticmethod
    def find_antinode_spot(
            loc1: tuple[int, int], loc2: tuple[int, int],
            x: int, y: int,
            p2: bool = False
    ):
        diff = (loc2[0] - loc1[0], loc2[1] - loc1[1])
        new_locs = []
        if p2:
            i = 0
            while True:
                new_loc = (loc2[0] + i * diff[0], loc2[1] + i * diff[1])
                if not (0 <= new_loc[0] < x and 0 <= new_loc[1] < y):
                    break
                new_locs.append(new_loc)
                i += 1
            i = 0
            while True:
                new_loc = (loc1[0] - i * diff[0], loc1[1] - i * diff[1])
                if not (0 <= new_loc[0] < x and 0 <= new_loc[1] < y):
                    break
                new_locs.append(new_loc)
                i += 1
        else:
            i = 1
            new_loc = (loc2[0] + i * diff[0], loc2[1] + i * diff[1])
            if (0 <= new_loc[0] < x and 0 <= new_loc[1] < y):
                new_locs.append(new_loc)
            new_loc = (loc1[0] - i * diff[0], loc1[1] - i * diff[1])
            if (0 <= new_loc[0] < x and 0 <= new_loc[1] < y):
                new_locs.append(new_loc)

        return new_locs

    def _solve_p1(self, inp: str) -> str:
        parsed = self.read_input(inp)
        antinode_spots = set()
        for char, locs_list in parsed["locs"].items():
            for i in range(len(locs_list)):
                for j in range(i + 1, len(locs_list)):
                    new_antinode_spots = self.find_antinode_spot(
                        locs_list[i], locs_list[j], parsed["y"], parsed["x"]
                    )
                    for n in new_antinode_spots:
                        antinode_spots.add(n)

        print(antinode_spots)
        return str(len(antinode_spots))

    def _solve(self, inp: str) -> str:
        parsed = self.read_input(inp)
        antinode_spots = set()
        for char, locs_list in parsed["locs"].items():
            for i in range(len(locs_list)):
                for j in range(i + 1, len(locs_list)):
                    new_antinode_spots = self.find_antinode_spot(
                        locs_list[i], locs_list[j], parsed["y"], parsed["x"], p2=True
                    )
                    for n in new_antinode_spots:
                        antinode_spots.add(n)

        print(antinode_spots)
        return str(len(antinode_spots))
