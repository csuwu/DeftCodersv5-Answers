import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        String aa = sc.nextLine().toLowerCase().trim();

        char[] data = aa.toCharArray();
        if(data.length<100){
        int a = 0, e = 0, ii = 0, o = 0, u = 0;
        for (int i = 0; i < data.length; i++) {

            if (data[i] == 'a') {
                a++;
            }
            if (data[i] == 'e') {
                e++;
            }
            if (data[i] == 'i') {
                ii++;
            }
            if (data[i] == 'o') {

                o++;
            }
            if (data[i] == 'u') {
                u++;
            }

        }

        System.out.println("a - " + a);
        System.out.println("e - " + e);
        System.out.println("i - " + ii);
        System.out.println("o - " + o);
        System.out.println("u - " + u);
        }

    }
}
