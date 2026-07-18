class Solution {
    public List<List<Integer>> printGraph(int V, int edges[][]) {
        
        // Step 1: create the outer list (one slot per node)
        List<List<Integer>> adj = new ArrayList<>();

        // Step 2: fill each slot with an empty list (one per node)
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        // Step 3: go through every edge and add neighbors both ways
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];   // first node of the edge
            int v = edges[i][1];   // second node of the edge

            adj.get(u).add(v);     // u is connected to v
            adj.get(v).add(u);     // since undirected, v is also connected to u
        }

        // Step 4: return the completed adjacency list
        return adj;
    }
}