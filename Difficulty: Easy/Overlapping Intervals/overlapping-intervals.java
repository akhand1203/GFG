class Solution {
	static boolean isIntersect(int[][] a) {
		// Code Here
		Arrays.sort(a, (x, y) -> x[0] - y[0]);
		int st1 = a[0][0];
		int end1 = a[0][1];
		for (int i = 1; i<a.length; i++) {
			int st2 = a[i][0];
			int end2 = a[i][1];
			if (end1 >= st2) {
				return true;
			}
			st1 = st2;
			end1 =Math.max(end1,end2);
		}
		return false;
	}
}
