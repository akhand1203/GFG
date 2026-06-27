class Solution {
    boolean fun(int[] a, int students, int mid, int n) {
        int s = 1;          
        int page = 0;

        for (int i = 0; i < n; i++) {
            if (page + a[i] <= mid) {
                page = page + a[i];
            } else {
                s++;
                page = a[i];
                if (s > students) {   
                    return false;
                }
            }
        }
        return true;
    }

    public int findPages(int[] a, int k) {
        int n = a.length;

        if (k > n) return -1;  

        int low = 0;
        int high = 0;

        for (int i = 0; i < n; i++) {
            low = Math.max(low, a[i]);  
            high = high + a[i];          
        }

        int res = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (fun(a, k, mid, n)) {
                res = mid;           
                high = mid - 1;     
            } else {
                low = mid + 1;  
            }
        }

        return res;
    }
}