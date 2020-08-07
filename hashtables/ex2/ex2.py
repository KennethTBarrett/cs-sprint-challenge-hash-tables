class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Setup
    route = [None] * length
    cache = {}

    # For all of the tickets we have...
    for ticket in tickets:
        # Set the ticket source in our cache to be our destination
        cache[ticket.source] = ticket.destination
    
    # Because our final destination must be "NONE"
    next = cache['NONE']

    # Iterate through, adding stop.
    for current in range(length):
        route[current] = next
        next = cache[next]
    return route  # Return our route