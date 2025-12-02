from math import log10, floor, ceil
from itertools import combinations_with_replacement

def main(input_path: str = "inputs/02/sample.txt") -> None:
    input_data: str
    with open(input_path) as f:
        input_data = f.read()

    print([(r.start, r.stop) for r in process_input(input_data)])
    ranges: list[range] = process_input(input_data)
    part1(ranges)

def process_input(input_data: str) -> list[range]:
    return [range(int(line.split("-")[0]), int(line.split("-")[1]) + 1) for line in input_data.split(",")]


def invalid_id_generator(r: range) -> int:
    power_of_10_start: int = floor(log10(r.start))
    power_of_10_stop: int = ceil(log10(r.stop))
    print(f"Generating invalid IDs between {r.start} and {r.stop}, powers {power_of_10_start} to {power_of_10_stop}")

    for power in range(power_of_10_start, power_of_10_stop + 1):
        if power % 2 == 0:
            continue
        repeat_length: int = power // 2
        for first_digit in range(1, 10):
            for combo in combinations_with_replacement(range(0, 10), repeat_length):
                half_id_digits = [str(first_digit)] + [str(d) for d in combo]
                half_id_str = "".join(half_id_digits)
                full_id_str = half_id_str + half_id_str
                full_id_int = int(full_id_str)
                if full_id_int in r:
                    yield full_id_int


def part1(ranges: list[range]) -> None:
    invalid_ids: list[int] = []
    for r in ranges:
        print(f"Processing range {r.start}-{r.stop}: {list(invalid_id_generator(r))}")
        invalid_ids.extend(list(invalid_id_generator(r)))

    print(f"Sum of invalid product Ids: {sum(invalid_ids)}")
    return

"""
All inputs between 10 digits.
0-9: 0 (not even) 10^0
10-99: 9 (multiples of 11) 10^1
100-999: 0 ( not even) 10^2
1000-9999: 90 ()"XYXY" 9 ops for X, 10 for Y) 10^3
10000-99999: 0 (not even) 10^4
100000-999999: 900 ( "XYZXYZ" 9 ops for X, 10 for Y, 10 for Z) 10^5
...


|Power of 10|Count of Even Repeats|Options|
|-----------|---------------------|-------|
|0          |0                    |X      |
|1          |9                    |1      |
|2          |0                    |X      |
|3          |90                   |2      |
|4          |0                    |X      |
|5          |900                  |3      |
|6          |0                    |X      |
|7          |9000                 |4      |
|8          |0                    |X      |
|9          |90000                |5      |
"""

if __name__ == "__main__":
    main()