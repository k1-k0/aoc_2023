import sys


def get_raw_data_from_file(filename: str) -> list[str]:
    with open(file=filename) as f:
        return f.read().splitlines()


def find_calibration_value(calibration: str) -> int:
    p1, p2 = 0, len(calibration) - 1
    digit1, digit2 = "", ""

    while p1 != p2 and calibration[p1].isdigit() is False:
        p1 += 1
    
    digit1 = calibration[p1]

    while p2 != p1 and calibration[p2].isdigit() is False:
        p2 -= 1
    
    if p1 != p2:
        digit2 = calibration[p2]

    if digit1 and not digit2:
        digits = [digit1, digit1]
    elif not digit1 and digit2:
        digits = [digit2, digit2]
    else:
        digits = [digit1, digit2]

    return int("".join(digits))


def find_sum_of_calibration_values(source: str) -> int:
    raw_data = get_raw_data_from_file(filename=source)
    
    calibration_values: list[int] = []
    for raw_calibration in raw_data:
        calibration_value = find_calibration_value(calibration=raw_calibration)
        print(raw_calibration, calibration_value)
        calibration_values.append(calibration_value)
    
    return sum(calibration_values)


if __name__ == "__main__":
    filename = sys.argv[1]
    print(find_sum_of_calibration_values(source=filename))