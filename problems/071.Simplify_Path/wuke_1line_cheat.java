public class Solution {
    public String simplifyPath(String path) {
        return java.nio.file.Paths.get(path).normalize().toString()
    }
}
