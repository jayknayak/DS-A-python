# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

from collections import OrderedDict


if __name__ == '__main__':
    s = input()
    string_list = sorted(s)
    string_dict = OrderedDict()
    for i in range(len(string_list)):
        if string_list[i] not in string_dict:
            string_dict[string_list[i]] = 1
        else:
            string_dict[string_list[i]] += 1
    sorted_string_dict = dict(sorted(string_dict.items(), key=lambda item: item[1], reverse=True))
    i=0
    for k, v in sorted_string_dict.items():
        if i==3:
            break
        print(k, v)
        i+=1


# Alternative solution using Counter:
from collections import Counter


if __name__ == '__main__':
    s = input()
    sorted_string_dict = sorted(Counter(s).items(), key=lambda item: (-item[1], item[0]))
    for k, v in sorted_string_dict[:3]:
        print(k, v)

