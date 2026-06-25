class Solution {
    public int findCeil(int[] a, int x) {
        // code here
        int n=a.length;
        int low=0;
        int high=n-1;
        int res=-1;
        while(low<=high){
            int mid=(low+high)/2;
            if(a[mid]<x){
                low=mid+1;
            }
            else{
                res=mid;
                high=mid-1;
            }
        }
        return res;
    }
}
