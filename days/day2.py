from math import log10, floor, ceil
from itertools import product
from typing import Generator

def main(input_path: str = "inputs/02/sample.txt") -> None:
    input_data: str
    with open(input_path) as f:
        input_data = f.read()

    ranges: list[range] = process_input(input_data)
    part1(ranges)
    part2(ranges)

def process_input(input_data: str) -> list[range]:
    return [range(int(line.split("-")[0]), int(line.split("-")[1]) + 1) for line in input_data.split(",")]


def invalid_id_generator(r: range) -> Generator[int, None, None]:
    power_of_10_start: int = floor(log10(r.start))
    power_of_10_stop: int = ceil(log10(r.stop))

    for power in range(power_of_10_start, power_of_10_stop + 1):
        if power % 2 == 0:
            continue
        repeat_length: int = power // 2
        for first_digit in range(1, 10):
            for combo in product(range(0, 10), repeat=repeat_length):
                half_id_digits = [str(first_digit)] + [str(d) for d in combo]
                half_id_str = "".join(half_id_digits)
                full_id_str = half_id_str + half_id_str
                full_id_int = int(full_id_str)
                if full_id_int in r:
                    yield full_id_int

def invalid_id_generator_part2(r: range) -> Generator[int, None, None]:
    start_str: str = str(r.start)
    stop_str: str = str(r.stop)
    start_digit_length: int = len(start_str)
    end_digit_length: int = len(stop_str)

    for length in range(max(start_digit_length, 2), end_digit_length + 1):
        for first_digit in range(1, 10):
            # Repeats of size 1, 2, 3, 4, ..., length // 2
            max_repeat_length: int = length // 2
            for chunk_size in range(1, max_repeat_length + 1):
                for combo in product(range(0, 10), repeat=chunk_size - 1):
                    chunk_digits: str = "".join([str(first_digit)] + [str(d) for d in combo])
                    full_id_str: str = chunk_digits * (length // chunk_size)
                    full_id_int = int(full_id_str)
                    if full_id_int in r:
                        yield full_id_int


def part1(ranges: list[range]) -> None:
    invalid_ids: list[int] = []
    for r in ranges:
        invalid_ids.extend(list(invalid_id_generator(r)))

    print(f"Sum of invalid product Ids: {sum(invalid_ids)}")
    return

def part2(ranges: list[range]) -> None:
    invalid_ids: list[int] = []
    for r in ranges:
        invalid_ids.extend(set(invalid_id_generator_part2(r)))

    print(f"Sum of invalid product Ids: {sum(invalid_ids)}")
    return

if __name__ == "__main__":
    main()