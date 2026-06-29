class Solution {
    public int firstSearch(int[] arr, int k) {
        // Code Here
         int n=arr.length;
        int low =0 , hi=n-1 , ind=-1;
        while(low<=hi){
            int mid=(low+hi)/2;
            if(arr[mid]>k) hi=mid-1;
            else if(arr[mid]<k) low=mid+1;
            else{
                ind=mid;
                hi=mid-1;
            }
            
        }
        return ind;
    }
}