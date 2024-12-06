from Problem import ProblemClass

IS_LOOP = -2


class Problem6(ProblemClass):
    initial_loc: tuple[int, int]
    initial_dir_idx: int
    y: int
    x: int
    obstacles: set[tuple[int, int]]
    directions: list[tuple[int, int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def read_input(self, inp: str):
        lines = inp.splitlines()
        obstacles = set()
        chars = "^>V<"
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in ["^", ">", "V", "<"]:
                    initial_loc = j, i
                    initial_dir = chars.find(char)
                if char == "#":
                    obstacles.add((j, i))

        self.initial_loc = initial_loc
        self.initial_dir = initial_dir
        self.obstacles = obstacles
        self.y = len(lines)
        self.x = len(lines[0])

    def rotate(self, current_dir_idx: int) -> int:
        return

    def visit_next_loc(
            self,
            current_loc: tuple[int, int],
            current_dir_idx: int,
):
        # print(current_loc, current_dir_idx)
        direction = self.directions[current_dir_idx]
        next_loc = current_loc[0] + direction[0], current_loc[1] + direction[1]
        if (
                next_loc[0] < 0 or next_loc[0] == self.x or
                next_loc[1] < 0 or next_loc[1] == self.y
        ):
            return None
        if next_loc in self.obstacles:
            current_dir_idx = (current_dir_idx + 1) % 4
        else:
            current_loc = next_loc

        return current_loc, current_dir_idx

    def visit_loop(self) -> set[tuple[int, int]]:
        # print(f"{self.obstacles=}")
        current_loc = self.initial_loc
        current_dir = self.initial_dir
        visited = set()
        visited.add((current_loc, current_dir))
        while True:
            output = self.visit_next_loc(current_loc, current_dir)
            if not output: # i stepped out
                break
            current_loc = output[0]
            current_dir = output[1]
            if (current_loc, current_dir) in visited:
                return IS_LOOP
            visited.add((current_loc, current_dir))

        return set([v[0] for v in visited])

    def _solve_p1(self, inp: str) -> str:
        self.read_input(inp)
        visited = self.visit_loop()
        return str(len(visited))


    def _solve(self, inp: str) -> str:
        self.read_input(inp)
        all_visited = self.visit_loop()
        num_potential_obstacles = 0
        for visited_loc in all_visited:
            # print(f"testing {visited_loc}")
            self.obstacles.add(visited_loc)
            output = self.visit_loop()
            if output == IS_LOOP:
                # print(f'loop {visited_loc}')
                num_potential_obstacles += 1

            self.obstacles.remove(visited_loc)

        return str(num_potential_obstacles)
