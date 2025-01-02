import java.math.BigDecimal;
import java.math.RoundingMode;
import java.math.MathContext;


public class Problem323 {
	
	public static void main(String[] args){
		BigDecimal expected = new BigDecimal("0");
		BigDecimal singleProbability = new BigDecimal("0.5");
		BigDecimal thisProbability = new BigDecimal("0");
		BigDecimal previousProbability = new BigDecimal("0");
		for (BigDecimal i = new BigDecimal("1"); i.compareTo(new BigDecimal("100"))<0; i=i.add(BigDecimal.ONE)){
			previousProbability = thisProbability;
			thisProbability = BigDecimal.ONE.subtract(singleProbability).pow(32);
			singleProbability = singleProbability.divide(new BigDecimal("2"), 40, RoundingMode.DOWN);
			expected = expected.add(thisProbability.subtract(previousProbability).multiply(i));
		}
		System.out.println(expected.round(new MathContext(11, RoundingMode.HALF_UP)));
	}
}
