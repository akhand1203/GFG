class Solution {
	public int minMeetingRooms(int[] a, int[] b) {
		Arrays.sort(a);
		Arrays.sort(b);
		
		int i = 0;
		int j = 0;
		int room = 0;
		int res = 0;
		
		while (i < a.length) {
			if (a[i] < b[j]) {
				room++;
				res = Math.max(res, room);
				i++;
			} else {
				room--;
				j++;
			}
		}
		
		return res;
	}
}
