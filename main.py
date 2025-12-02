import days
from argparse import ArgumentParser, Namespace as ArgNamespace

class MainArguments(ArgNamespace):
    day: int
    input_type: str

    def __init__(self, args: ArgNamespace):
        self.day = args.day
        self.input_type = args.input_type
        super()

def main(args: MainArguments):

    input_path: str = f"inputs/{str(args.day).rjust(2, '0')}/{'input' if args.input_type in ['a', 'actual'] else 'sample'}.txt"

    if (args.day == 1):
        days.d1(input_path)


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        prog = "Advent of Code 2025",
    )

    parser.add_argument(
        "day",
        type=int,
    )

    parser.add_argument(
        "--input-type",
        "-it",
        "-in",
        type=str,
        choices=["sample", "s", "actual", "a"],
        default="sample"
    )

    args: MainArguments = MainArguments(parser.parse_args())
    main(args)
