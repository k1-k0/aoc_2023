import sys

word2digit: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_raw_data_from_file(filename: str) -> list[str]:
    with open(file=filename) as f:
        return f.read().splitlines()


def find_calibration_value(calibration: str) -> int:
    digit1, digit2 = "", ""

    cursor = 0
    while cursor < len(calibration):
        part = calibration[:cursor]
        for word in word2digit.keys():
            if word in part:
                digit1 = word2digit[word]
                break

        if digit1:
            break

        if calibration[cursor].isdigit():
            digit1 = calibration[cursor]
            break

        cursor += 1

    cursor = 1
    while cursor < len(calibration):
        part = calibration[-cursor:]
        for word in word2digit.keys():
            if word in part:
                digit2 = word2digit[word]
                break
        
        if digit2:
            break

        if calibration[-cursor].isdigit():
            digit2 = calibration[-cursor]
            break

        cursor += 1

    if digit1 and not digit2:
        digits = [digit1, digit1]
    elif not digit1 and digit2:
        digits = [digit2, digit2]
    else:
        digits = [digit1, digit2]

    return int(f"{digits[0]}{digits[1]}")


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