import sys


NOTHING = "."
GEAR = "*"


def get_raw_lines_from_file(filename: str) -> list[str]:
    with open(file=filename) as f:
        return f.read().splitlines()


def build_matrix_from_inputs(inputs: list[str]) -> list[list[str]]:
    matrix: list[list[str]] = [
        [NOTHING for _ in range(len(inputs[0]))]
        for _ in range(len(inputs))
    ]
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            matrix[i][j] = inputs[i][j]
    return matrix


def find_sum_of_parts(matrix: list[list[str]]) -> int:
    result = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != GEAR:
                continue

            pos = is_any_digit_around(i, j, matrix)
            if pos is None:
                continue

            fi, fj = pos[0], pos[1]
            number1 = find_full_number(fi, fj, matrix)

            pos2 = is_any_digit_around(i, j, matrix, fi, fj)
            if pos2 is None:
                continue

            si, sj = pos2[0], pos2[1]
            number2 = find_full_number(si, sj, matrix)

            if number1 is not None and number2 is not None:
                result += (number1 * number2)

    return result


def is_any_digit_around(
    i: int,
    j: int,
    matrix: list[list[str]],
    fi: int | None = None,
    fj: int | None = None,
) -> tuple[int, int] | None:
    si, sj = i - 1, j
    if i > 0 and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i + 1, j
    if si < len(matrix) and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i, j - 1
    if j > 0 and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i - 1, j - 1
    if i > 0 and j > 0 and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i + 1, j - 1
    if i + 1 < len(matrix) and j > 0 and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i, j + 1
    if j + 1 < len(matrix[i]) and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i - 1, j + 1
    if i > 0 and j + 1 < len(matrix[i]) and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    si, sj = i + 1, j + 1
    if i + 1 < len(matrix) and j + 1 < len(matrix[i]) and matrix[si][sj].isdigit():
        if (fi is None and fj is None) or ((fi, fj) != (si, sj) and (abs(fi - si) == 2 or abs(fj - sj) == 2)):
            return (si, sj)

    return None


def find_full_number(i: int, j: int, matrix: list[list[str]]) -> int | None: 
    while j > 0 and matrix[i][j - 1].isdigit():
        j -= 1

    digits = ""
    while j < len(matrix) - 1 and matrix[i][j + 1].isdigit():
        digits += matrix[i][j]
        j += 1

    digits += matrix[i][j]

    return int(digits)


if __name__ == "__main__":
    filename = sys.argv[1]
    inputs = get_raw_lines_from_file(filename=filename)
    matrix = build_matrix_from_inputs(inputs=inputs)
    print(find_sum_of_parts(matrix=matrix))
