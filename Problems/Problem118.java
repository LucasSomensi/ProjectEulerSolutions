import java.util.HashMap;
import java.math.BigInteger;

public class Problem118 {
	
	public static HashMap<Integer, Boolean> primes;
	
	public static boolean isPrime(int n){
		if (n<2) return false;
		if (n==2 || n==3) return true;
		if (n%2==0 || n%3==0) return false;
		if (primes.containsKey(n)) return primes.get(n);
		boolean result;
		BigInteger bigN = new BigInteger(String.valueOf(n));
		result = bigN.isProbablePrime(15);
		primes.put(n, result);
		return result;
	}

	public static boolean isValid(int permutation, int mask){
		int[] set = new int[9];
		int count = 0;
		int temp = permutation%10;
		permutation = permutation/10;
		for (int i = 0; i<8; i++){
			if (mask%2==1){
				if (count>0 && temp<set[count-1]) return false;
				if (!isPrime(temp)) return false;
				set[count] = temp;
				temp = 0;
				count++;
			}
			temp = 10*temp + permutation%10;
			permutation = permutation/10;
			mask = mask/2;
		}
		if (temp!=0) set[count] = temp;
		if (count>0 && (set[count]<set[count-1])) return false;
		if (temp!=0 && (!isPrime(temp))) return false;
		return true;
	}
	
	
	public static void main (String[] args){
		
		int[] permutations = new int[362880];
		int count;
		boolean[][] usedDigits = new boolean[365880][9];
		
		
		//ugly code, but it works
		int period = 362880;
		int power = 1000000000;
		for (int i = 9; i>=1; i--){
			period = period/i;
			power = power/10;
			int digit = i;
			for (count = 0; count<362880; count++){
				if (count%period==0) digit = (i==1)?1:digit%i+1;
				int j = 0;
				int thisCount = 0;
				while (thisCount!=digit){
					if (!usedDigits[count][j]) thisCount+=1;
					j++;
				}
				usedDigits[count][j-1] = true;
				permutations[count] += j*power;
			}
		}
		usedDigits = null;
		
		
		primes = new HashMap<Integer, Boolean>();
		int result = 0;
		for (int i = 0; i<362880; i++){
			for (int mask = 0; mask<256; mask++){
				if (isValid(permutations[i], mask)) result++;
			}
		}
		System.out.println("Result: " + result);
		
	}
	
}
