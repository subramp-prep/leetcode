public class Solution {

  public String reverseWords(String s) {
    String[] parts = s.trim().split("\\s+");
    String out = "";
    for (int i = parts.length - 1; i > 0; i--) {
        out += parts[i] + " ";
    }
    return out + parts[0];
  }
}

// https://discuss.leetcode.com/topic/2742/my-accepted-java-solution