public class Solution {
    public String convertTo7(int num) {
        return Integer.toString(num, 7);
    }
}
//The formula for converting from one base to another is:
//Integer.toString(Integer.parseInt(number, base1), base2);