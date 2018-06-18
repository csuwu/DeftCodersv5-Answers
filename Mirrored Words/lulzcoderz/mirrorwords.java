import java.util.*;
class  mirror{
public static void main(String []args){
 Scanner in = new Scanner(System.in);
 String str = in.nextLine();
 StringBuffer buffer=new StringBuffer(str).reverse();
 System.out.println(buffer.toString());
}
}
