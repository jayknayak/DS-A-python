# https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true
import collections

def matchingStrings(stringList, queries):
    string_list_count = collections.Counter(stringList)
    return [string_list_count[query] for query in queries]
