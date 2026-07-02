class Solution {

    class Node {
        int value;
        int row;
        int col;
        Node(int v, int r, int c) {
            value = v;
            row = r;
            col = c;
        }
    }
    static class Compare implements Comparator<Node> {
        @Override
        public int compare(Node a, Node b) {
            return a.value - b.value;
        }
    }
    public ArrayList<Integer> mergeArrays(int[][] mat) {
        ArrayList<Integer> res = new ArrayList<>();
        int n = mat.length;
        int m = mat[0].length;
        PriorityQueue<Node> pq = new PriorityQueue<>(new Compare());
        for (int i = 0; i < n; i++) {
            pq.add(new Node(mat[i][0], i, 0));
        }
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            res.add(node.value);
            int col = node.col;
            if (col == m - 1)
                continue;
            pq.add(new Node(mat[node.row][col + 1], node.row, col + 1));
        }
        return res;
    }
}