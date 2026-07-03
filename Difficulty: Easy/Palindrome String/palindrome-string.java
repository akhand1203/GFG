class Solution {
    boolean isPalindrome(String s) {
        int n = s.length() - 1;
        return fun(s, 0, n);
    }

    boolean fun(String s, int low, int high) {
        int len = high - low + 1;
        if (len <= 1) {
            return true;
        }
        if (s.charAt(low) != s.charAt(high)) {
            return false;
        }
        return fun(s, low + 1, high - 1);
    }
}