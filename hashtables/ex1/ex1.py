def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    # Iterate through range(length)
    # by our index, adding existing weights
    # by index.
    for i in range(length):
        cache[weights[i]] = i

    # Find weights already in cache.
    for index, weight in enumerate(weights):
        target_weight = limit - weight  # Subtract weight from limit.
        # Check if that value is in cache. If it is...
        if target_weight in cache:
            i = cache[target_weight]  # Set i to its value
            # And return with the appropriate formatting.
            return (i, index) if index < i else (index, i)