import java.util.Map;
import java.util.HashMap;

public class Solution {
    public int longestConsecutive(int[] nums) {
        final int length = nums.length;
        if (length <= 1) return length;

        final Map<Integer, Integer> elementIndexMap = new HashMap();
        final UnionFind uf = new UnionFind(length);
        for (int p = 0; p < length; p++) {
            final int i = nums[p];
            if (elementIndexMap.containsKey(i)) continue;
            if (elementIndexMap.containsKey(i+1)) uf.union(p, elementIndexMap.get(i+1));
            if (elementIndexMap.containsKey(i-1)) uf.union(p, elementIndexMap.get(i-1));
            elementIndexMap.put(i, p);
        }
        return uf.getHighestRank();
    }

    private final class UnionFind {
        final private int[] sequenceTree;
        final private int[] rank;
        private int highestRank;

        UnionFind(int length) {
            sequenceTree = new int[length];
            rank = new int[length];
            highestRank = 1;
            for (int i = 0; i < length; i++) {
                sequenceTree[i] = i;
                rank[i] = 1;
            }
        }

    void union(int p, int q) {
            final int pId = find(p); final int qId = find(q);

            if (pId == qId) return;

            int localHighestRank = 1;
            if (rank[pId] < rank[qId]) {
                sequenceTree[pId] = qId;
                rank[qId] += rank[pId];
                localHighestRank = rank[qId];
            } else {
                sequenceTree[qId] = pId;
                rank[pId] += rank[qId];
                localHighestRank = rank[pId];
            }
            highestRank = Math.max(highestRank, localHighestRank);
        }

        int find(int p) {
            while (p != sequenceTree[p]) {
                sequenceTree[p] = sequenceTree[sequenceTree[p]];
                p = sequenceTree[p];
            }
            return p;
        }

        int getHighestRank() { return highestRank; }
    }
}