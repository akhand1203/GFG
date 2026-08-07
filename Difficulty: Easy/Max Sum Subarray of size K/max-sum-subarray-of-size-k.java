class Solution {
    public int maxSubarraySum(int[] nums, int k) {
        // Code here
        int wsum=0;
        for(int i=0;i<k;i++){
            wsum=wsum+nums[i];
        }
        int res=wsum;
        for(int j=k;j<nums.length;j++){
            wsum=wsum+nums[j];
            wsum=wsum-nums[j-k];
            res=Math.max(wsum,res);
        }
        return res;
    }
}