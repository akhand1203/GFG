class Solution {
    public ArrayList<Integer> bfs(ArrayList<ArrayList<Integer>> adj) {
        int n = adj.size();
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<Boolean> vis = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            vis.add(false);
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        vis.set(0, true);

        while (!q.isEmpty()) {
            int node = q.peek();
            q.poll();
            res.add(node);

            for (int i = 0; i < adj.get(node).size(); i++) {
                int neigh = adj.get(node).get(i);
                if (vis.get(neigh) == false) {
                    q.add(neigh);
                    vis.set(neigh, true);
                }
            }
        }
        return res;
    }
}