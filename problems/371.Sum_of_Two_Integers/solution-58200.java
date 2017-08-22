public class Solution {
    public int getSum(int a, int b) {
        return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
    }
}


// c stands for the carry bit of adding two integers.
// The sum of two integers can be decomposed into a summation bit (a & b)
// and a carry bit (a ^ b). The << 1 is to set the carry bit to the correct bit.
// The above process is repeated until no carry (c, stored in b, becomes 0).
// Then the sum is stored in a.