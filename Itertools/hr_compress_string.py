# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

from itertools import groupby


def compress_the_string():
    grouped_str = groupby(input_str)
    output_str = ''
    for k, g in grouped_str:
        key_length = str(len(list(g)))
        output_str = output_str + '(' + key_length + ', ' + str(k) + ') '
    print(output_str)


input_str = input()
compress_the_string()
