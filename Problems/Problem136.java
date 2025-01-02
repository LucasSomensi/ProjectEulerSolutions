
public class Problem136 {
    
    public static final int target = 1;
    public static final int range = 50000000;
    
    public static void main(String[] args){
        
        byte[] oneSolution = new byte[range+1];
        
        for (int i = 1; i<=range; i++){
            long sq = (long)i * (long)i;
            int last = range - (range%i);
            last -= i*((last/i+i)%4);
            for (int n = last; 3L*(long)n>sq; n-=4*i){
                if (oneSolution[n]<=target){
                    oneSolution[n]++;
                }
            }
        }
        
        int count = 0;
        for (int k = 1; k<=range; k++){
            if (oneSolution[k]==target) {
                count++; 
            }
        }
        System.out.println(count);
        
    }
}
