class Solution {
    public boolean isSorted(int[] a) {
        // code here
        int n=a.length;
        return fun(a,0,n);
        
    }
    boolean fun(int[] a,int i,int n){
        if(i==n || i==n-1){
            return true;
        }
        if(a[i]>a[i+1]){
            return false;
        }
        return fun(a,i+1,n);
    }
}