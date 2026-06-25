class Solution {
    public ArrayList<Integer> preGreaterEle(int[] a) {

        Stack<Integer> st = new Stack<>();
        ArrayList<Integer> res = new ArrayList<>();

        res.add(-1);
        st.push(a[0]);

        for (int i = 1; i < a.length; i++) {

            while (!st.isEmpty() && st.peek() <= a[i]) {
                st.pop();
            }

            if (st.isEmpty()) {
                res.add(-1);
            } else {
                res.add(st.peek());
            }

            st.push(a[i]);
        }

        return res;
    }
}