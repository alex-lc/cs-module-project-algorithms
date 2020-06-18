'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # loop through the array
    # in each iteration, create a temporary list of the current value,
    # plus the next values in the array based on the window size
    # find the max value in the temporary list and return it
    max_nums = []
    for i in range(len(nums) - (k-1)):
        sublist = nums[i:i+k]
        max_val = max(sublist)
        max_nums.append(max_val)

    return max_nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
