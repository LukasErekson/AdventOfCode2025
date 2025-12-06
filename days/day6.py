
def main(input_path: str = "inputs/06/sample.txt") -> None:
    input_data: str
    with open(input_path) as f:
        input_data = f.read()

    input_lines: list[str] = input_data.split("\n")
    number_lines: list[str] = input_lines[:-1]
    numbers: list[list[int]] = [[int(num) for num in line.split()] for line in number_lines]
    operator_line: list[str] = input_lines[-1].split()

    part1(numbers, operator_line)
    part2(number_lines, operator_line)

def part1(numbers: list[list[int]], operator_line: list[str]) -> None:
    answers: list[int] = numbers[0]

    for number_list in numbers[1:]:
        for i in range(len(number_list)):
            if operator_line[i] == "+":
                answers[i] += number_list[i]
            else:
                answers[i] *= number_list[i]

    print(f"The grand total of the answers is {sum(answers)}")

    return

def part2(number_lines: list[str], operator_line: list[str]) -> None:
    answers: list[int] = [0 if op == "+" else 1 for op in operator_line]

    operator_index: int = -1

    for column_index in range(-1, -len(number_lines[0]) - 1, -1):
        column: str = ""
        for line in number_lines:
            column += line[column_index]
        column = column.replace(" ", "")
        if column == "":
            operator_index -= 1
            continue

        operand: int = int(column)

        if (operator_line[operator_index] == "+"):
            answers[operator_index] += operand
        else:
            answers[operator_index] *= operand

    print(f"The grand total of the problems the proper way is {sum(answers)}")
    return

if __name__ == "__main__":
    main()