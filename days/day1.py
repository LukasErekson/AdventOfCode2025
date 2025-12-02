from argparse import ArgumentParser, Namespace


def main(input_path: str) -> None:
    input: str
    with open(input_path) as f:
        input = f.read()

    turns: list[int] = process_input(input)

    part1(turns)
    part2(turns)

    return


def process_input(input: str) -> list[int]:
    return list(map(int, input.replace("R", "").replace("L", "-").split()))


def part1(turns: list[int]) -> None:
    zero_counts: int = 0
    position: int = 50

    for turn in turns:
        position += turn
        position %= 100
        if position == 0:
            zero_counts += 1

    print(f"The number of times the dial points at 0 is {zero_counts}")
    return


def sign(n: int) -> int:
    return 1 if n >= 0 else -1


def part2(turns: list[int]) -> None:
    zero_passes: int = 0
    current_position: int = 50

    for turn in turns:
        while abs(turn) >= 100:
            turn -= sign(turn) * 100
            zero_passes += 1
        new_position: int = current_position + turn

        if current_position != 0 and (new_position <= 0 or new_position >= 100):
            zero_passes += 1

        current_position = new_position % 100

    print(f"The number of times the dial passes 0 is {zero_passes}")

    return


class Day1Arguments:
    file_path: str

    def __init__(self, args: Namespace):
        self.file_path = args.filepath


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        prog="Advent of Code 2024 Day 1",
        description="Solving Advent of Code Day 1",
    )

    parser.add_argument("filepath")
    args = Day1Arguments(parser.parse_args())

    main(args.file_path)
