int bestRotation(int* A, int N) {
    int best_score = 0, best_K = 0, score;
    for (int K = 0; K < N; K++) {
        score = 0;
        for (int i = 0; i < N; i++)
            if (A[(K + i) % N] <= i) score++;
        if (score > best_score) {
            best_K = K;
            best_score = score;
        }
    }
    return best_K;
}