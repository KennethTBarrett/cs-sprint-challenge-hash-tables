def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}
    # Check each number in each subarray
    # If the number isn't in the cache
    # Make it an entry
    for subarray in arrays:
        for number in subarray:
            if number not in cache:
                # Its irrelevant what we set
                # this value to, as we're going to
                # be simply making a dict from our keys
                # (using dict as a set essentially).
                cache[number] = number
            else:
                # If it is in the cache, append
                # to `result` array.
                result.append(number)
    # Make list w/ dictionary using the keys in `result`
    result = list(dict.fromkeys(result))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
