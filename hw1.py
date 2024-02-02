#!/usr/bin/env python
"""Reference solution for HW1.

I just use built-in Python libraries, but you are welcome to use third-party
libraries if you wish."""


import argparse
import csv
import math
import operator


def _read_freqs(path: str) -> dict[str, int]:
    """Reads TSV frequency tables into dictionary."""
    freqs: dict[str, int] = {}
    with open(path, "r") as source:
        for word, freq in csv.reader(source, delimiter="\t"):
            freqs[word] = int(freq)
    return freqs


def _get_n(freqs: dict[str, int]) -> int:
    """Computes the # of tokens."""
    return sum(freqs.values())


# Here I am using the formula:
#
#    log c_1 + log(N_2 - c_2) - log c_2 - log(N_1 - c_1)
#
# but I give three other equivalent options in the slides.


def _log_odds_ratio(c1: int, n1: int, c2: int, n2: int) -> float:
    """Computes log-odds ratio."""
    return math.log(c1) + math.log(n2 - c2) - math.log(c2) - math.log(n1 - c1)


def main(args: argparse.Namespace) -> None:
    # Gets frequency distributions and the denominators.
    freqs1 = _read_freqs(args.tsv1)
    freqs2 = _read_freqs(args.tsv2)
    n1 = _get_n(freqs1)
    n2 = _get_n(freqs1)
    # Builds ratio table.
    log_odds_ratios: list[tuple[str, float]] = []
    for word, c1 in freqs1.items():
        try:
            c2 = freqs2[word]
            lor = _log_odds_ratio(c1, n1, c2, n2)
            log_odds_ratios.append((word, lor))
        except KeyError:
            pass
    # Gets extreme values.
    # In-place `list.sort` is faster than out-of-place `sorted`, since it
    # doesn't have to allocate extra memory. The `key` argument says that
    # we are sorting by the second element of the tuple. NB: this is where
    # one would use `heapq.nlargest` and `heapq.nsmallest` if one attempts
    # that relevant stretch goal.
    log_odds_ratios.sort(key=operator.itemgetter(1))
    print(f"{args.n} lowest log-odds ratio terms:")
    for word, lor in log_odds_ratios[: args.n]:
        print(f"{word}\t{lor:.4f}")
    print()
    print(f"{args.n} highest log-odds ratio terms:")
    for word, lor in log_odds_ratios[-args.n:]:
        print(f"{word}\t{lor:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Shows terms with extreme log-odds ratio values"
    )
    parser.add_argument("tsv1")
    parser.add_argument("tsv2")
    parser.add_argument(
        "--n",
        type=int,
        default=10,
        help="# of terms to show (default: %(default)s)",
    )
    main(parser.parse_args())
