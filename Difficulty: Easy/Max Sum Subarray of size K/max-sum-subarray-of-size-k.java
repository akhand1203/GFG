class Solution {
    public int maxSubarraySum(int[] arr, int k) {
        int low = 0;
        int high = k;
        int sum = 0;
        int res = 0;
        int n = arr.length;

        for (int i = 0; i < k; i++) {
            sum = sum + arr[i];
        }

        res = sum;

        while (high < n) {
            sum = sum - arr[low]; 
            sum = sum + arr[high];    
            res = Math.max(res, sum);
            low++;
            high++;
        }

        return res;
    }
}