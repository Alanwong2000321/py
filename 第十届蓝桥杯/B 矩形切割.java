import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = sc.nextInt();
        int min=sc.nextInt();
        int count=0,num,temp;
        while (true){
            if ( min==0){//当没有得时候就可以退出了
                break;
            }
            num =  max/min;//看看当前长宽不变得时候有几个正方形
            count+=num;    //把这些都加进来
            //替换一下，剪完正方形，之后，原来得长就变成了宽，原来的宽就成了长
            temp=max-min*num;//原来得长减去剪掉得几个宽，就是现在得宽
            max=min;
            min=temp;

        }
        System.out.println(count);
    }
        }