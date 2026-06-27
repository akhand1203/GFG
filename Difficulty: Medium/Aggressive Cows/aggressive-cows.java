class Solution {
	boolean fun(int[]a, int n, int k, int mid) {
		int cow = 1;
		int pos = a[0];
		for (int i = 1; i<n; i++) {
			int dis = a[i]-pos;
			if (dis<mid) {
				continue;
			}
			cow++;
			pos = a[i];
		}
		if (cow >= k) {
			return true;
		}
		else {
			return false;
		}
		
	}
	public int aggressiveCows(int[] a, int k) {
		// code here
		int n = a.length;
		Arrays.sort(a);
		int low = 1;
		int high = a[n - 1]-a[0];
		int res = -1;
		while (low <= high) {
			int mid = low + (high - low)/2;
			if (fun(a, n, k, mid)) {
				res = mid;
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		return res;
	}
}
