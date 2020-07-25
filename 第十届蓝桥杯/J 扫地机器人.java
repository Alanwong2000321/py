 

import java.util.Scanner;

public class 扫地机器人_c {
	static int N;
	static int K;
	static int[] a = new int[1000000];
	static int[] b = new int[1000000];

	public static void main(String[] args) {
		int i,L;
		Scanner sc =new Scanner(System.in);
		N=sc.nextInt();
		K=sc.nextInt();
		for (  i = 1; i <=K; i++) {
			a[i]=sc.nextInt();
			b[a[i]]=1;
		}
		L=fun();
		System.out.println(2*(L-1));
		
	}
	
	
public static	boolean check1(int first_L, int L) { //第一个区间长度为 first_L，之后区间长度都为 L
		int i, j;
		if (first_L + (K - 1) * L < N) {//第一个区间再加上，其他的机器人和*这段的长度是不是能够够到总长
			return false;
		}
		i = 1; //第 i 个区间
		j = 1; //当前查看的方格位置
		while (j <= N) {
			if (b[j] == 1) { //第 i 个区间内有机器人
				j = first_L + (i - 1) * L + 1; //j 指向下一个区间起点
				i++; //下一个区间
			}
			else {
				j++;//一直检查下一个方格，如果一直没有直到first_L和j相等后，表明真的没有机器人
				if (j == first_L + (i - 1) * L + 1 || j == N + 1) { //第 i 个区间内没有机器人
					return false;		//因为L是不断变大的，first也一直变大，所以检查一直再往后扩展
				}
			}
		}
		return true;
	}
public static		boolean check(int L) {
		int first_L; //首区间的长度(取值范围：1~L)
		for (first_L = L; first_L > 0; first_L--) {//倒叙是因为，用大区间可以减少机器人的移动
			if (check1(first_L, L)) {
				return true;
			}
		}
		return false;
	}
public static		int fun() {
		int i, j, L;
		for (L = N / K; L <= N; L++) {//平均一下，
			if (check(L)) {
				return L;
			}
		}
		return L;
	}

}

