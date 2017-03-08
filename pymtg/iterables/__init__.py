def chunks(l, n):
    """Yield successive ``n``-sized chunks from ``l``.

    Examples:
        >>> list(chunks([1, 2, 3, 4, 5], 2))
        [[1, 2], [3, 4], [5]]
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]
