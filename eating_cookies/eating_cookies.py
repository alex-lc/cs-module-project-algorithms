'''
Input: an integer
Returns: an integer
'''


# Day 1:
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


# Day 2:
def eating_cookies(n, cache={}):
    # base cases
    if n < 0:
        return 0

    if n == 0:
        return 1

    # does n exist in our cache?
    if cache and n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(
            n-3) + eating_cookies(n-2) + eating_cookies(n-1)

    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
