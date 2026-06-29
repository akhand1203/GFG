class Solution {
    int missingNum(int arr[]) {
        // code here
        int n = arr.length;
        int arrsum=0;
       for(int i=0;i<=n+1;i++){
            arrsum+=i;
       }
        int sum=0;
        for(int i=0;i<=n-1;i++){
            sum+=arr[i];
        }
        return arrsum-sum;
    }
}