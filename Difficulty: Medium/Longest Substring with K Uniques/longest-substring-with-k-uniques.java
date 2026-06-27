class Solution {
	public int longestKSubstr(String s, int k) {
		int low = 0;
		int high = 0;
		int n = s.length();
		int res = -1;
		HashMap<Character, Integer> f = new HashMap<>();
		for (high = 0; high<n; high++) {
			
			char ch = s.charAt(high);
			int count = f.getOrDefault(ch, 0);
			f.put(ch, count + 1);
			while (f.size()>k) {
				char c = s.charAt(low);
                f.put(c, f.get(c) - 1);
                if (f.get(c) == 0) f.remove(c);
					low++;
				}
				if (f.size() == k) {
					int len = high - low + 1;
					res = Math.max(len, res);
				}
			}
			return res;
		}
	}

