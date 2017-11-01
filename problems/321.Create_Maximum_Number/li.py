def castleTowers(n, ar):
    ar.sort(reverse=True)
    maxi = int(ar[0])
    count = 1
    for x in xrange(1, len(ar)):
        if maxi == ar[x]:
            count += 1
    return count
