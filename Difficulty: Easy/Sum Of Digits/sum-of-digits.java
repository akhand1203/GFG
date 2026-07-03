class Solution {
    static int sumOfDigits(int n) {
        // code here
       if(n==0){
           return 0;
       }
       int d=n%10;
       n=n/10;
       int ans=sumOfDigits(n);
       return ans+d;
    }
}
