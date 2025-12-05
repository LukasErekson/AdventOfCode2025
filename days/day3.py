
def main(input_path: str = "inputs/03/input.txt") -> None:
    raw_input: str
    with open(input_path, "r") as f:
        raw_input = f.read()

    battery_banks: list[str] = raw_input.split("\n")

    part1(battery_banks)
    part2(battery_banks)

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

    for bank in battery_banks:
        joltages.append(int(largest_joltage(bank)))

    print(f"Part 2: The sum of the joltages is {sum(joltages)}")


def largest_joltage(sub_bank: str, joltage: str = "", at_least_remaining: int = 11) -> str:
    # Base case: All that's left is what can be
    if len(sub_bank) == at_least_remaining or at_least_remaining == -1:
        return joltage
    
    # Find max digit in sub_bank
    max_digit: str = max(sub_bank)
    max_digit_idx: int = sub_bank.index(max_digit)
    sub_sub_bank: str = sub_bank[max_digit_idx + 1:]

    while len(sub_sub_bank) < at_least_remaining:
        max_digit = max(sub_bank[:max_digit_idx])
        max_digit_idx = sub_bank.index(max_digit)
        sub_sub_bank = sub_bank[max_digit_idx + 1:]

    return largest_joltage(sub_sub_bank, joltage + max_digit, at_least_remaining - 1)


if __name__ == "__main__":
    main()