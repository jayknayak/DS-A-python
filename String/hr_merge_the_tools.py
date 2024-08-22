# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    # your code goes here
    substr_count = int(len(string) / k)

    j = 0
    for i in range(0, substr_count):
        substr = string[j:j + k]
        result_str = ''
        for z in range(0, len(substr)):
            if substr[z] not in result_str:
                result_str = result_str + substr[z]
        print(result_str)
        j = j + k



string, k = 'AABCAAADA', 3
merge_the_tools(string, k)