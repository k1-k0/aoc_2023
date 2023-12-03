from enum import StrEnum
import sys


class Color(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


def get_raw_lines_from_file(filename: str) -> list[str]:
    with open(file=filename) as f:
        return f.read().splitlines()


def find_max_count_of_each_color(set_of_cubes: list[str]) -> tuple[int, int, int]:
    reds, greens, blues = 0, 0, 0

    for cubes in set_of_cubes:
        if reds and greens and blues:
            break

        count = int(cubes.split()[0])
        if not reds and Color.RED in cubes:
            reds = count
            continue
        if not greens and Color.GREEN in cubes:
            greens = count
            continue
        if not blues and Color.BLUE in cubes:
            blues = count
            continue
    
    return (reds, greens, blues)


def pick_out_sets(line: str) -> list[str]:
    game_name_prefix_lenght = line.index(":") + 2

    sets = []
    for subset_of_cubes in line[game_name_prefix_lenght:].split(";"):
        for cubes in subset_of_cubes.split(","):
            sets.append(cubes.strip())

    sets.sort(key=lambda value: int(value.split(" ")[0]), reverse=True)
    return sets


def find_sum_of_maxes(inputs: list[str]) -> int:
    sum_of_games = 0

    for game, line in enumerate(inputs, start=1):
        set_of_cubes = pick_out_sets(line=line)
        r, g, b = find_max_count_of_each_color(set_of_cubes=set_of_cubes)
        sum_of_games += (r * g * b)

    return sum_of_games


if __name__ == "__main__":
    filename = sys.argv[1]
    inputs = get_raw_lines_from_file(filename=filename)
    print(find_sum_of_maxes(inputs=inputs))
