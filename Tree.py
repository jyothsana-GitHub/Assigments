def problem(n, edges):
    return n - len(edges) - 1

if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    edges = []
    for i in range(1, len(dataset)):
        edges.append(map(int, dataset[i].split()))
    print (problem(10, [(1, 2), (2, 8), (4, 10), (5, 9), (6, 10), (7, 9)]))
