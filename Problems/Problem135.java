
public class Problem135 {
    
    public static final int target = 10;
    public static final int range = 1000000;
    
    public static void main(String[] args){
        int n = 2;
        int total = 0;
        while (n<range){
            int count = 0;
            for (int i = 1; 4*n>(i*i+n); i++){
                if (n%i==0 && (n/i+i)%4==0) {
                    count++;
                }
            }
            if (count==target) total+=1;
            n++;
        }
        System.out.println(total);
    }
    
}
