
def main(input_path: str = "inputs/03/input.txt") -> None:
    raw_input: str
    with open(input_path, "r") as f:
        raw_input = f.read()

    battery_banks: list[str] = raw_input.split("\n")

    part1(battery_banks)

    return

def part1(battery_banks: list[str]) -> None:
    joltages: list[int] = []

    for bank in battery_banks:
        first_digit: str = max(bank[:-1])
        second_digit: str = max(bank[bank.index(first_digit) + 1:])
        joltage: int = int(f"{first_digit}{second_digit}")

        joltages.append(joltage)

    print(f"Part 1:The sum of the joltages is {sum(joltages)}")


def part2(battery_banks: list[str]) -> None:
    joltages: list[int] = []

    print(f"Part 2: The sum of the joltages is {sum(joltages)}")


if __name__ == "__main__":
    main()