import java.math.BigInteger;
import java.util.HashSet;

public class Problem131 {
    
    public static final long limit = 1000000;
    
    public static boolean isPrime(long n){
        if (n<=1L) return false;
        if (n==2L || n==3L) return true;
        if (n%2L==0 || n%3L==0) return false;
        BigInteger bigN = new BigInteger(String.valueOf(n));
        return bigN.isProbablePrime(30);
    }
    
    public static void main(String[] args){
        HashSet<Long> counted = new HashSet<Long>();
        int count = 0;
        for (long a = 2; a*a*a-(a-1)*(a-1)*(a-1)<limit; a++){
            for (long b = a-1; a*a*a-b*b*b<limit; b--){
                long p = a*a*a-b*b*b;
                if (isPrime(p) && !counted.contains(p)) {
                    counted.add(p);
                    count++;
                }
            }
        }
        System.out.println("Result: " + count);
    }
    
}
