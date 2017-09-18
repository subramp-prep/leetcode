Incrementing all but one is equivalent to decrementing that one. So let's do that instead. How many single-element decrements to make all equal? No point to decrementing below the current minimum, so how many single-element decrements to make all equal to the current minimum? Just take the difference from what we currently have (the sum) to what we want (n times the minimum).

Python:

def minMoves(self, nums):
    return sum(nums) - len(nums) * min(nums)
Ruby:

def min_moves(nums)
  nums.inject(:+) - nums.size * nums.min
end
Java (ugh :-):

public int minMoves(int[] nums) {
    return IntStream.of(nums).sum() - nums.length * IntStream.of(nums).min().getAsInt();
}
C++ (more ugh):

int minMoves(vector<int>& nums) {
    return accumulate(begin(nums), end(nums), 0L) - nums.size() * *min_element(begin(nums), end(nums));
}
(edit: I changed 0 to 0L because it failed the apparently added testcase [1,2147483647])