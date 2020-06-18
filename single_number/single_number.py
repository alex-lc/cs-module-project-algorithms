'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# Day 1:
# def single_number(arr):
#     # loop through array
#     # if the count of the current item is only equal to 1,
#     # then return that individual value
#     for i in arr:  # O(n)
#         if arr.count(i) == 1:  # O(n)
#             return i

# Day 2:
def single_number(arr):

    # create a dictionary to hold our duplicate counts
    dupes = {}

    for num in arr:
        # check if num is in our dictionary
        if num in dupes:
            # delete it from the dictionary
            del dupes[num]
        else:
            # add it to the dictionary and set its value to 1
            dupes[num] = 1

    for key, val in dupes.items():
        if val == 1:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
