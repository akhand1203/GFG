class Solution {
    void segregate0and1(int[] arr) {
        int i = 0;
        int j = 1;

        while (j < arr.length) {
            if (arr[i] == 1 && arr[j] == 0) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j++;
            } else if (arr[i] == 0) {
                i++;                 
                j++;
            } else {
                j++;        
            }
        }
    }
}