    class Solution {
        public List<String> letterCasePermutation(String S) {
            List<String> a = new ArrayList<>();
            dfs(S.toCharArray(), 0, a);
            return a;
        }

        void dfs(char[] s, int pos, List<String> a)
        {
            if(pos == s.length){
                a.add(new String(s));
                return;
            }
            dfs(s, pos+1, a);
            if(s[pos] >= 'A' && s[pos] <= 'Z' ||
                    s[pos] >= 'a' && s[pos] <= 'z'){
                s[pos] ^= 32;
                dfs(s, pos+1, a);
            }
        }
    }