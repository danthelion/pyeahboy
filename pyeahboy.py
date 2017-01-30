#!/usr/bin/env python3

import argparse


def yeah_boy(max_len: int, yeah_to_boy_ratio: float):
    """
    Yeah boiiiiii.

    :param max_len: Maximum length of the "Yeah, Boy!".
    :param yeah_to_boy_ratio: "Yeah" to "Boy" ratio.
    :return: Formatted "Yeah, Boy!"
    """
    _max_len = max_len - 10
    _yeah = int(_max_len * yeah_to_boy_ratio)
    _boy = int(_max_len * (1 - yeah_to_boy_ratio))
    yeah_boy_result = 'Ye{}ah, Bo{}y!'.format('e' * _yeah, 'o' * _boy)

    return yeah_boy_result


def main():
    """
    Parse CLI arguments and call main business logic.
    :return:
    """
    parser = argparse.ArgumentParser(description='Generate your longest "Yeah Boy" ever!')
    parser.add_argument('-l', '--len', type=int, default=11, help='Maximum length of the "Yeah Boy".')
    parser.add_argument('-r', '--ratio', type=float, default=0.1, help='"Yeah" to "Boy" ratio.')
    args = parser.parse_args()

    if args.ratio < 0 or args.ratio > 1:
        print('Invalid ratio! 0 < r < 1')
        return None

    yeah_boy_result = yeah_boy(max_len=args.len, yeah_to_boy_ratio=args.ratio)

    print(yeah_boy_result)


if __name__ == "__main__":
    main()
