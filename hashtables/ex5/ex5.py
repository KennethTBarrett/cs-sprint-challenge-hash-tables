def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    # For every item in the files, we need to
    # make our split, and append the item if
    # in cache.
    for path in files:
        # Get final part, set as item, check
        # if in cache.
        item = path.split('/')[-1]
        if item in cache:
            cache[item].append(path)
        else:
            cache[item] = [path]
    # For every query we have, check if it's in the cache.
    # If the query exists in our cache, we're going to append
    # the path of the results of that query of our cache.
    result = []
    for query in queries:
        if query in cache:
            results = cache[query]
            for path in results:
                result.append(path)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
