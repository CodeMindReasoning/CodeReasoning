class main:
    import java.util.Scanner;
    
    public class p03485 {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            int a = sc.nextInt();
            int b = sc.nextInt();
    
            System.out.println(solve(a, b));
    
            sc.close();
        }
    
        static int solve(int a, int b) {
            return (a + b + 1) // 2;
        }
    }