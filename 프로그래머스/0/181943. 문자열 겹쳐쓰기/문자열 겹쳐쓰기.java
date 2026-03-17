class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        char c;
        for(int i=0;i<my_string.length();i++){
            if(s<=i && i<overwrite_string.length()+s){
                c=overwrite_string.charAt(i-s);
            } else {
                c=my_string.charAt(i);
            }
            answer+=c;
        }
        return answer;
    }
}
