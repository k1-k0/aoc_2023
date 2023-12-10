import sys


NOTHING = "."


def get_raw_lines_from_file(filename: str) -> list[str]:
    with open(file=filename) as f:
        return f.read().splitlines()


def get_win_and_yours_numbers(card: str) -> tuple[list[int], list[int]]:
    lists = card[card.find(":") + 2:].split("|")
    wins = [int(n) for n in lists[0].split()]
    yours = [int(n) for n in lists[1].split()]
    return wins, yours


def get_total_points(inputs: list[str]) -> int:
    scores: dict[int, int] = {i+1: 1 for i in range(len(inputs))}

    for index, card in enumerate(inputs, start=1):
        wins, yours = get_win_and_yours_numbers(card=card)
        matches = len([n for n in yours if n in wins])
        for m in range(matches):
            scores[index + 1 + m] += 1 * scores[index]

    return sum(scores.values())


if __name__ == "__main__":
    filename = sys.argv[1]
    inputs = get_raw_lines_from_file(filename=filename)
    print(get_total_points(inputs=inputs))
