'''
Input: a List of integers
Returns: a List of integers
'''

# Day 1:
# def moving_zeroes(arr):
#     # loop through the array
#     # if the current item == 0, remove it and append it to the end of the list
#     for i in arr:  # O(n)
#         if i == 0:
#             arr.remove(i)  # O(n)
#             arr.append(0)  # O(n)

#     return arr

# Day 2:
def moving_zeroes(arr):

    # left pointer at the beginning
    # right pointer at the end
    # loop until left and right pointers meet or right pointer passes left
    # right pointer is less than left pointer
    left = 0
    right = len(arr) - 1

    for i in range(right):
        if arr[left] == 0:
            arr.append(0)
            del arr[left]
            right -= 1
        else:
            left += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
