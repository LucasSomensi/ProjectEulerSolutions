import java.util.ArrayList;
import java.lang.Math;
import java.math.BigInteger;


public class Problem387 {
    
    public static final int NDIGITS = 14;
    
    public static boolean isHashad(long n){
        long sum = n%10L;
        long temp = n/10L;
        while (temp!=0L){
            sum += temp%10L;
            temp = temp/10L;
        }
        return (n%sum==0L);
    }
    
    public static boolean isPrime(long n){
    	if (n<2L) return false;
    	if (n==2L||n==3L) return true;
    	if (n%2L==0L || n%3L==0L) return false;
    	//Fermat primality testing to eliminate most composites
    	BigInteger temp = new BigInteger(String.valueOf(n));
    	if (!temp.isProbablePrime(10)) return false;
    	//If it reaches this point, it is probably prime, but we have to make sure
    	for (long d = 5L; d<=(long)Math.sqrt(n); d+=2L){
    		if (n%d==0L) return false;
    	}
    	return true;
    }
    
    public static boolean isStrongHashad(long n){
    	long sum = n%10L;
    	long remainder = n/10L;
    	while (remainder!=0L){
    		sum += remainder%10L;
    		remainder = remainder/10L;
    	}
    	if (n%sum!=0L) return false;
    	return (isPrime(n/sum));
    }
    
    public static long[] filterStrongHashad(long[] weakHashad){
    	long[] temp = new long[weakHashad.length];
    	int count = 0;
    	for (int i = 0; i<weakHashad.length; i++){
    		if (isStrongHashad(weakHashad[i])) {
    			temp[count]=weakHashad[i];
    			count += 1;
    		}
    	}
    	long[] result = new long[count];
        for (int i = 0; i<count; i++){
        	result[i] = temp[i];
        }
        return result;
    }
    
    public static long[] addNext(long[] hashad){
    	ArrayList<Long> resultList = new ArrayList<Long>();
    	long[] result;
        for (int i = 0; i<hashad.length; i++){
            for (int j = 0; j<10; j++){
                long temp = hashad[i]*10L+(long)j;
                if (isHashad(temp)) resultList.add(temp);
            }
        }
        result = new long[resultList.size()];
        for (int i = 0; i<resultList.size(); i++){
        	result[i] = resultList.get(i);
        }
        return result;
    }
    
    public static void main(String[] args){
        long[][] hashad = new long[NDIGITS-1][];
        hashad[0] = new long[] {1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 9L};
        for (int i = 2; i<=NDIGITS-1; i++){
            hashad[i-1] = addNext(hashad[i-2]);
            hashad[i-2] = filterStrongHashad(hashad[i-2]);
        }
        hashad[NDIGITS-2] = filterStrongHashad(hashad[NDIGITS-2]);
        
        
        long total = 0L;
        for (int i = 0; i<hashad.length; i++){
        	for (int j = 0; j<hashad[i].length; j++){
        		if (isPrime(hashad[i][j]*10L+1L)) total+= hashad[i][j]*10L+1L;
        		if (isPrime(hashad[i][j]*10L+3L)) total+= hashad[i][j]*10L+3L;
        		if (isPrime(hashad[i][j]*10L+7L)) total+= hashad[i][j]*10L+7L;
        		if (isPrime(hashad[i][j]*10L+9L)) total+= hashad[i][j]*10L+9L;
        	}
        }
        System.out.println(total);
        
    }
}
