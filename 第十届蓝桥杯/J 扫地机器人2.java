public class j十扫地机器人 {
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n=scanner.nextInt();
		int k=scanner.nextInt();
		int c[]=new int[k];
		for (int i = 0; i <k; i++) {
			c[i]=scanner.nextInt();
		}
		Arrays.sort(c);
		int len;
		if(n%k==0)len=n/k;
		else len=n/k+1;
		len=Math.max(len, c[0]+1);
		int m;//区域的边界
		for (int i = len; i < n; i++) {
			m=0;
			for (int j = 0; j < k; j++) {
				if(m>c[j])m=Math.max(m, c[j]+i);
				else m+=i;
				if (m<c[j]) break;	
			}
			if(m>=n) {System.out.println((i-1)*2);break;}
		}
		
	}
}