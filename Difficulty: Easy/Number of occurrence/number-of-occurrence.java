class Solution {
    int countFreq(int[] a, int target) {
        // code here
        int first = find(a, target, true);
        if (first == -1) return 0;
        int last = find(a, target, false);
        return last-first+1;
    }
    private int find(int[] a, int x, boolean findFirst) {
        int low = 0, high = a.length - 1, res = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (a[mid] < x) {
                low = mid + 1;
            } else if (a[mid] > x) {
                high = mid - 1;
            } else {
                res =mid;
                if (findFirst)
                    high = mid - 1;
                else
                    low = mid + 1;
            }
        }
        return res;
    }
}
