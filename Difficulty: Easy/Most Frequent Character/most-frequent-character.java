class Solution {
    public char getMaxOccuringChar(String s) {
        // code here
        int n = s.length();
        int[] freq = new int[26];
        for(int i=0;i<n;i++){
            char ch = s. charAt(i);
            int idx = ch-'a';
            freq[idx]++;
        }
            int maxFreq = 0;
            char ans = s.charAt(0);
        for(int i=0;i<26;i++){
            if(freq[i]>maxFreq){
            maxFreq = freq[i];
            ans = (char)(i + 97);
            }
    }
    return ans;
}
}