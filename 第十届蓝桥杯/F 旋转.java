import java.util.*;
//对于这种题，作者认为最好的方法就是用笔和纸在纸上写一遍
//把旋转过来的左边写一下，看看对应的是原来的哪一个坐标
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int [][] num = new int [n+1][m+1];
        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=m; j++) {
                num[i][j]=sc.nextInt();
            }
        }
        int [][]shu = new int [m+1][n+1];
        for (int i = 1; i <=m; i++) {
            for (int j = 1; j <=n; j++) {
                shu[i][j]=num[n-j+1][i];       //关键点在这
            }
        }
        for (int i = 1; i <=m; i++) {
            for (int j = 1; j <=n; j++) {
                System.out.print(shu[i][j]+" ");
            }
            System.out.println();
        }
    }
}
