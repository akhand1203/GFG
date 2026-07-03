class Solution {
    public void removeCharacter(StringBuilder s, char c) {
        int n = s.length();
        StringBuilder result = new StringBuilder();
        fun(s, n, 0, c, result);
        s.setLength(0);
        s.append(result);
    }

    void fun(StringBuilder s, int n, int i, char c, StringBuilder result) {
        if (i == n) {
            return;
        }
        if (s.charAt(i) != c) {
            result.append(s.charAt(i));
        }
        fun(s, n, i + 1, c, result);
    }
}