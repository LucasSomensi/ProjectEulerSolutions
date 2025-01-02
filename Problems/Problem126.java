
public class Problem126 {
	
	public static void main(String[] args){
		int limit = 20000;
		int[] result = new int[limit+1];
		for (int sum = 3; 2*(2*(sum-2)+1)<=limit; sum++){
			for (int a = sum-2; 3*a>=sum; a--){
				int maxb = Math.min(a, sum-a-1);
				int minc = sum - a - maxb;
				if (2*(a*maxb+a*minc+maxb*minc)>limit) break;
				for (int b = maxb; b>=(sum-a-b); b--){
					int c = sum - a - b;
					int crossmult = a*b+b*c+a*c;
					if (2*crossmult>limit) break;
					for (int n = 1; (2*crossmult+4*(n-1)*sum+4*n*n-12*n+8)<=limit; n++){
						result[2*crossmult+4*(n-1)*sum+4*n*n-12*n+8] += 1;
					}
				}
			}
		}
		
		for (int i = 0; i<result.length; i++){
			if (result[i]==1000) {
				System.out.println("Result: " + i);
				break;
			}
		}
		
	}
	
}
