#create CLI tool to extract/fetch data from xkcd.com

import argparse

if __name__ == "__main__":
    example = """
    example:
    python task one max 87 n any 15
     """
    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resoucres from API",
        epilo=example
    )

    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max no. of resources fetched"
    )
    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunk of res to be fetched "
    )

    args = parser.parse_args()
    print(args)
    print(type(args))
    print(dir(args))
    print(parser.print_help())
    print(parser.print_help())