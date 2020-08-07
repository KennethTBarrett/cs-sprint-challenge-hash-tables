def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}
    # Make entries for each number in our cache.
    for number in a:
        cache[number] = number
    # Go through the cache. If the number * -1 exists
    # in our cache, then we'll append it to our result
    # array.
    for number in a:
        if number * -1 in cache and number > 0:
            result.append(number)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
