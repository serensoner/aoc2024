from collections import deque
from dataclasses import dataclass
from typing import Optional, Any

from Problem import ProblemClass



class Problem23(ProblemClass):
    nodes: dict[str, list[str]]


    def read_input(self, inp: str) -> None:
        self.nodes = {}
        for line in inp.splitlines():
            parts = line.split("-")
            # if not (parts[0].startswith("t") or parts[1].startswith("t")):
            #     continue

            if parts[0] not in self.nodes:
                self.nodes[parts[0]] = []
            if parts[1] not in self.nodes:
                self.nodes[parts[1]] = []

            self.nodes[parts[0]].append(parts[1])
            self.nodes[parts[1]].append(parts[0])

    def _solve_p1(self, inp: str) -> str:
        self.read_input(inp)
        circles_of_3 = set()
        for node, node_set in self.nodes.items():
            if not node.startswith("t"):
                continue
            num_elems = len(node_set)
            if num_elems < 2:
                continue
            for i in range(num_elems):
                for j in range(i + 1, num_elems):
                    if node_set[j] in self.nodes[node_set[i]]:
                        set_of_elems = ",".join(sorted([node, node_set[i], node_set[j]]))
                        circles_of_3.add(set_of_elems)

        print(circles_of_3)
        return str(len(circles_of_3))

    def _solve(self, inp: str) -> str:
        self.read_input(inp)
        largest_circle = set()
        for node, node_set in self.nodes.items():
            current_circle = {node}
            for node2 in node_set:
                for nodes_in_circle in current_circle:
                    if node2 not in self.nodes[nodes_in_circle]:
                        break
                else:
                    current_circle.add(node2)
            if len(current_circle) > len(largest_circle):
                largest_circle = current_circle

        return ','.join(sorted(list(largest_circle)))
