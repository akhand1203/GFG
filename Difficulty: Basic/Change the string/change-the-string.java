// User function Template for Java

class Solution {
    String modify(String s) {
        if(s.length()==0){
            return "";
        }
       int x=(int)s.charAt(0);
        if(x>=65&&x<=90){
          return s.toUpperCase();
        }
        else{
               return s.toLowerCase();
        }
    }
}