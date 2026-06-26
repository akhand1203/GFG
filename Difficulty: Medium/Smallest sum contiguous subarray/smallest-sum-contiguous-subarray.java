class Solution {
    static int smallestSumSubarray(int a[], int size) {
        // your code here
        int i=0;
        int bestend=a[0];
        int ans=a[0];
        for(i=1;i<a.length;i++){
            int v1=bestend+a[i];
            int v2=a[i];
            bestend=Math.min(v1,v2);
            ans=Math.min(bestend,ans);
        }
        return ans;
    }
}