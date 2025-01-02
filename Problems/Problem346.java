public class Problem346 {
	
	
	public static void main(String[] args){
		
		
		long limit = 1000000000000L;
		long sum = 1L;
		long[] strongRepunit = new long[100000];
		long[] tempArray;
		int counter = 0;
		int oldCounter = 0;
		
		for (long b = 2L; b*b+b+1L<limit; b++){
			if (counter>=20000){
				tempArray = new long[100000];
				oldCounter = counter;
				counter = 0;
				for (int i = 0; i<=oldCounter; i++){
					if (strongRepunit[i]>=b*b+b+1L){
						tempArray[counter] = strongRepunit[i];
						counter++;
					} else {
						sum += strongRepunit[i];
					}
				}
				strongRepunit = tempArray;
			}
			for (long n = b*b+b+1L; n<limit; n = (n*b)+1L){
				boolean hasIt = false;
				for (int i = 0; strongRepunit[i]!=0; i++){
					if (strongRepunit[i]==n) {
						hasIt = true;
						break;
					}
				}
				if (!hasIt) {
					strongRepunit[counter] = n;
					counter+=1;
				}
			}
		}
		for (int i = 0; strongRepunit[i]!=0; i++){
			sum+=strongRepunit[i];
		}
		System.out.println("Soma: " + sum);
	}
}
