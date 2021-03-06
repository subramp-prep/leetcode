class Solution {
    public String mostCommonWord(String p, String[] banned) {
        Set<String> ban = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> count = new HashMap<>();
        String[] words = p.replaceAll("\\pP" , "").toLowerCase().split("\\s+");
        String res = "";
        int max = 0;
        for (String w : words) {
            if (!ban.contains(w)) {
                count.put(w, count.getOrDefault(w, 0) + 1);
                if (count.get(w) > max) {
                    res = w;
                    max = count.get(w);
                };
            };
        };
        return res;
    }
}