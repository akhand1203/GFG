class Solution {
    void dfs(ArrayList<ArrayList<Integer>> adj, int node, ArrayList<Integer> res, ArrayList<Boolean> vis) {
        res.add(node);
        vis.set(node, true);

        for (int i = 0; i < adj.get(node).size(); i++) {
            int neigh = adj.get(node).get(i);
            if (vis.get(neigh) == false) {
                dfs(adj, neigh, res, vis);
            }
        }
        return;
    }

    public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
        int n = adj.size();
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<Boolean> vis = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            vis.add(false);
        }
        dfs(adj, 0, res, vis);
        return res;
    }
}