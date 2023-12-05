import sys


NOTHING = "."


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
        part = ""
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                part += matrix[i][j]
                continue
            
            if len(part) > 0 and is_any_symbols_around(i, j-1, len(part), matrix):
                result += int(part)
                part = ""
            else:
                part = ""
        
        if len(part) > 0 and is_any_symbols_around(i, len(matrix[i])-1, len(part), matrix):
            result += int(part)

    return result


def is_any_symbols_around(i: int, j: int, part_len: int, matrix: list[list[str]]) -> bool:
    for k in range(part_len):
        pos = j - k
        if i > 0 and matrix[i - 1][pos] != NOTHING:
            return True
        if i + 1 < len(matrix) and matrix[i + 1][pos] != NOTHING:
            return True

        if k == part_len - 1:
            if pos > 0 and matrix[i][pos - 1] != NOTHING:
                return True
            if i > 0 and pos > 0 and matrix[i - 1][pos - 1] != NOTHING:
                return True
            if i + 1 < len(matrix) and pos > 0 and matrix[i + 1][pos - 1] != NOTHING:
                return True

        if k == 0:
            if pos + 1 != len(matrix[i]) and matrix[i][pos + 1] != NOTHING:
                return True
            if i > 0 and pos + 1 != len(matrix[i]) and matrix[i - 1][pos + 1] != NOTHING:
                return True
            if i + 1 < len(matrix) and pos + 1 != len(matrix[i]) and matrix[i + 1][pos + 1] != NOTHING:
                return True
        
    return False


if __name__ == "__main__":
    filename = sys.argv[1]
    inputs = get_raw_lines_from_file(filename=filename)
    matrix = build_matrix_from_inputs(inputs=inputs)
    print(find_sum_of_parts(matrix=matrix))
