// User function Template for Java

class Solution {
    static int evenlyDivides(int n) {
        // code here
        int m=n;
        int count=0;
          while(n !=0){
            int d = n%10;
             n = n/10;
            if(d!= 0 && m%d == 0){
             count++;
        }
       
    }
     return count;
}
}