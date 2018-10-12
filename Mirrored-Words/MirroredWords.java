import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
         String a=sc.nextLine();
     
         
       
String [] strArray = a.split("");
StringBuilder sb = new StringBuilder();
for(int i=strArray.length-1;i>-1;i--)
{
    sb.append(strArray[i]+"");
}
System.out.println(sb.toString());
    
    }
}