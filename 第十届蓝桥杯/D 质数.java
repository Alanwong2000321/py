import java.util.*;

public class Main {
    public static void main(String[] args) {
        int count = 0;int temp = 0;
        A:	for (int i = 2; ; i++) {
            for (int j = 2; j <i; j++) {
                if(i%j==0){

                    continue A;
                }
            }
            count++;
            if(count==2019){
                System.out.println(i);
                break;
            }
        }
    }
}
