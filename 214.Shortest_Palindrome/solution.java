public String shortestPalindrome(String s) {
    int i = 0, end = s.length() - 1, j = end; char chs[] = s.toCharArray();
    while(i < j) {
         if (chs[i] == chs[j]) {
             i++; j--;
         } else {
             i = 0; end--; j = end;
         }
    }
    return new StringBuilder(s.substring(end+1)).reverse().toString() + s;
}


// https://discuss.leetcode.com/topic/25860/my-9-lines-three-pointers-java-solution-with-explanation
// The key point is to find the longest palindrome starting from the first character,
// and then reverse the remaining part as the prefix to s. Any advice will be welcome!