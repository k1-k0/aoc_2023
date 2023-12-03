import sys


RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14


def get_raw_lines_from_file(filename: str) -> list[str]:
    with open(file=filename) as f:
        return f.read().splitlines()


def is_any_limit_in_set_of_cubes(set_of_cubes: list[str]) -> bool:
    for cubes in set_of_cubes:
        count = int(cubes.split()[0])

        if count < min([RED_LIMIT, GREEN_LIMIT, BLUE_LIMIT]):
            return False
        if "red" in cubes and count > RED_LIMIT:
            return True
        if "green" in cubes and count > GREEN_LIMIT:
            return True
        if "blue" in cubes and count > BLUE_LIMIT:
            return True

    return False


def pick_out_sets(line: str) -> list[str]:
    game_name_prefix_lenght = line.index(":") + 2

    sets = []
    for subset_of_cubes in line[game_name_prefix_lenght:].split(";"):
        for cubes in subset_of_cubes.split(","):
            sets.append(cubes.strip())

    print(sets)
    sets.sort(key=lambda value: int(value.split(" ")[0]), reverse=True)
    return sets


def find_sum_of_possible_games(inputs: list[str]) -> int:
    sum_of_games = 0

    for game, line in enumerate(inputs, start=1):
        set_of_cubes = pick_out_sets(line=line)
        if not is_any_limit_in_set_of_cubes(set_of_cubes=set_of_cubes):
            print(game)
            sum_of_games += game

    return sum_of_games


if __name__ == "__main__":
    filename = sys.argv[1]
    inputs = get_raw_lines_from_file(filename=filename)
    print(find_sum_of_possible_games(inputs=inputs))
