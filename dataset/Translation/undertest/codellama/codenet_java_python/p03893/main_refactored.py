class main:
    import java.util.Scanner;
    
    public class p03893 {
    	public static void main (String[] args) {
    		Scanner sc = new Scanner(System.in);
    		int x = sc.nextInt();
    		long next = 2;
    		for (int i = 0; i < x; i++) {
    			next = (next + 1) * 2;
    		}
    		System.out.println(next);
    	}
    }
    
    
    
    import sys
    
    x = int(sys.stdin.readline())
    next = 2
    for i in range(x):
        next = (next + 1) * 2
    print(next)