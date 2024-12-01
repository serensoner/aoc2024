from Problem import ProblemClass


def get_sum(line: str, include_words: bool) -> int:
    digits = []
    for i in range(len(line)):
        if line[i].isnumeric():
            digits.append(line[i])
            continue

        if include_words:
            words = {
                'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9
            }
            for word, num in words.items():
                if len(line) >= i + len(word) and line[i:i + len(word)] == word:
                    digits.append(str(num))
                    i = i + len(word)
                    continue

    if digits:
        return int(digits[0] + digits[-1])

    return 0


class Problem1(ProblemClass):
    def read_input(self, inp: str) -> tuple[list[int], list[int]]:
        lines = inp.splitlines()
        lists = [l.split("  ") for l in lines]
        return [int(l[0].strip()) for l in lists], [int(l[1].strip()) for l in lists]

    def _solve_p1(self, inp: str) -> str:
        lists = self.read_input(inp)
        lists[0].sort()
        lists[1].sort()
        print([abs(l2 - l1) for l1, l2 in zip(lists[0], lists[1])])
        return str(sum([l2 - l1 for l1, l2 in zip(lists[0], lists[1])]))

    def _solve(self, inp: str) -> str:
        lists = self.read_input(inp)
        counts = {}
        total = 0
        for l in lists[0]:
            if l not in counts:
                counts[l] = lists[1].count(l)
            total += l * counts[l]

        return total