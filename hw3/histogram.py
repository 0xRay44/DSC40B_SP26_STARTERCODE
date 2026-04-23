def histogram(points, bins):
    n = len(points)
    densities = []
    i = 0

    for a, b in bins:
        count = 0
        while i < n and points[i] < b:
            count += 1
            i += 1
        densities.append(count / (n * (b - a)))

    return densities
