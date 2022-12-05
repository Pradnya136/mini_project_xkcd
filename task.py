"""
CLI tool to fetch data from "https://xkcd.com/"

python task_one.py --max 87  --any 15
"""

import argparse
from random import randrange
from typing import List


def rand_gen(start: int = 1, stop: int = 87, limit: int= 15) -> List[int]:
  """

  Args:
      start:
      stop:
      limit:

  Returns:

  """


  random_n = randrange(start,stop + 1)   #stop is exclusive so did plus one
  return random_n

if __name__ == "__main__":
    example = """example:

    python task_one.py --max 87  --any 15
    """

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )

    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be fetched"
    )

    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunck of resources to be fetched"
    )

    args = parser.parse_args()
    print(args.any)
    print(args.max)

    print(parser.print_help())
    print(rand_gen(1, args.max, args.any))
#command to get args run = python task.py --max 150 --any 5