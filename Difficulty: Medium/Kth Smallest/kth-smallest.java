class Solution {
    public int kthSmallest(int[] a, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : a) {
            pq.add(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        return pq.peek();
    }
}