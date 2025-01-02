
public class Problem504 {
	
	public static final int mMax = 100;
	
	public static boolean isSquare(int n){
		for (int i = (int)Math.sqrt(n)-1; i*i<=n; i++){
			if (i*i==n) return true;
		}
		return false;
	}
	
	
	public static void main(String[] args){
		//building the array with the number of lattice points inside a triangle
		int[][] lattice = new int[mMax+1][mMax+1];
		for (int a = 1; a<=mMax; a++){ 				// a is the x intercept
			for (int b = 1; b<=mMax; b++){			// b is the y intercept
				int sum = 0;
				for (int x = 1; x<a; x++){		// the x coordinate of the point being tested
					for (int y = 1; y<b; y++){	// the y coordinate of the point being tested
						if ((b-y)*a > x*b) sum+=1;
					}
				}
				lattice[a][b] = sum;
			}
		}
		
	    int total = 0;
		for (int a = 1; a<=mMax; a++){
			for (int b = 1; b<=mMax; b++){
				for (int c = 1; c<=mMax; c++){
					for (int d = 1; d<=mMax; d++){
						int temp = lattice[a][b] + lattice[b][c] + lattice[c][d] + lattice[d][a] +
								a + b + c + d + 1 - 4;
						if (isSquare(temp)) {
							total++;
						}
					}
				}
			}
		}
		
		System.out.println("Total: " + total);
		
	}
	
	
}
