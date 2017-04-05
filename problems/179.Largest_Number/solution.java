public class Solution {
    public String largestNumber(int[] num) {
        String[] array = Arrays.stream(num).mapToObj(String::valueOf).toArray(String[]::new);
        Arrays.sort(array, (String s1, String s2) -> (s2 + s1).compareTo(s1 + s2));
        return Arrays.stream(array).reduce((x, y) -> x.equals("0") ? y : x + y).get();
    }
}

//https://discuss.leetcode.com/topic/7235/my-3-lines-code-in-java-and-python

//The logic is pretty straightforward. Just compare number by convert it to string.

//Thanks for Java 8, it makes code beautiful.

