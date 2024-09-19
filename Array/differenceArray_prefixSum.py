# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true
def arrayManipulation(n, queries):
    # Create an array of zeros with size n + 1 (1-indexed, so extra element for ease)
    arr = [0] * (n + 1)

    # Apply the difference array logic for each query
    for query in queries:
        a = query[0] - 1  # Convert to 0-indexed
        b = query[1] - 1  # Convert to 0-indexed
        k = query[2]

        arr[a] += k  # Start adding k from index a
        if b + 1 < n:
            arr[b + 1] -= k  # Stop adding k after index b

    # Compute the actual values using a prefix sum and find the maximum value
    max_value = 0
    current_value = 0
    print(arr)

    for i in range(n):
        current_value += arr[i]  # Apply the prefix sum to get the current value
        if current_value > max_value:
            max_value = current_value

    return max_value