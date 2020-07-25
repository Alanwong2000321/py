 


import java.util.Arrays;
import java.util.Scanner;

public class 等差数列2 {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int n = sc.nextInt();
        int [] num = new int [n];			//输入的数
        int [] cha = new int [n-1];			//数组排序后，相邻的数字最小的差值
        for (int i = 0; i < num.length; i++) {
            num[i]=sc.nextInt();
        }
        Arrays.sort(num);
        int min_cha=Integer.MAX_VALUE;
        for (int i=0;i<cha.length;i++){
            cha[i]=num[i+1]-num[i];
            min_cha=Math.min(cha[i],min_cha);
        }
//        for (int i:cha
//             ) {
//            System.out.println(i);
//        }
        int dengcha=Integer.MAX_VALUE;
       A: for (;min_cha>0;min_cha--){
            boolean bool = false;
            for (int i=0;i<cha.length;i++){
                if (cha[i]%min_cha!=0){
                    continue A;
                }
            }
            dengcha=min_cha;
            break A;
        }
//        System.out.println(dengcha);
        int num1 = num[num.length-1]-num[0];
        int count=1;
        count+=num1/dengcha;
        System.out.println(count);
    }
}

