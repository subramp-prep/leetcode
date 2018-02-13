bool hasAlternatingBits(int n) {
    return !((n ^= n/4) & n-1);
}

bool hasAlternatingBits(int n) {
    return !((n ^= n/2) & n+1);
}