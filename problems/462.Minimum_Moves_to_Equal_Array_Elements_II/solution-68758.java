public int minMoves2(int[] A) {
    int sum = 0, median = quickselect(A, A.length/2+1, 0, A.length-1);
    for (int i=0;i<A.length;i++) sum += Math.abs(A[i] - median);
    return sum;
}

public int quickselect(int[] A, int k, int start, int end) {
    int l = start, r = end, pivot = A[(l+r)/2];
    while (l<=r) {
        while (A[l] < pivot) l++;
        while (A[r] > pivot) r--;
        if (l>=r) break;
        swap(A, l++, r--);
    }
    if (l-start+1 > k) return quickselect(A, k, start, l-1);
    if (l-start+1 == k && l==r) return A[l];
    return quickselect(A, k-r+start-1, r+1, end);
}

public void swap(int[] A, int i, int j) {
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}