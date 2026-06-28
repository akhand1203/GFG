class Solution {
    public int kthSmallest(int[] a, int k) {
        // Code here
        PriorityQueue <Integer> pq=new PriorityQueue<>();
        for(int i=0;i<a.length;i++){
            pq.add(a[i]);
        }
        for(int i=1;i<k;i++){
            pq.poll();
        }
        int res=pq.peek();
        return res;
    }
}
