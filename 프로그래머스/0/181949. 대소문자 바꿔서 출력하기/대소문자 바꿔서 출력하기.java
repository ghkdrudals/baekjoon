import java.util.Scanner;
import java.util.InputMismatchException;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        for(int i=0;i<a.length();i++){
            char c = a.charAt(i);
            if (Character.isLowerCase(c)){
                String str = String.valueOf(c).toUpperCase();
                System.out.print(str);
            } else {
                String str = String.valueOf(c).toLowerCase();
                System.out.print(str);
            }
        }
    }
}