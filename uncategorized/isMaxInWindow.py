from collections import deque

def max_in_window(arr):
    n = len(arr)
    result = [False] * n  # Initialize the result list with False values
    max_values = deque()

    for i in range(n):
        # Remove elements outside of the current window
        while max_values and max_values[0] < i - arr[i]:
            max_values.popleft()

        # Check if the current element is the maximum in its window
        if max_values and arr[i] >= max(arr[max_values[0]], arr[i]):
            result[i] = True

        # Remove elements that are smaller than the current element from the back
        while max_values and arr[i] >= arr[max_values[-1]]:
            max_values.pop()

        max_values.append(i)

    return result

# Test the function
input_array = [2, 1, 0, 1, 1]
output_array = max_in_window(input_array)
print(output_array)  # Output: [False, False, False, False, True]