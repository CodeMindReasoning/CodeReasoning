class main:
    import java.util.*;
    class p03577{
        public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            String line = sc.next();
            int length = line.length();
            System.out.println(line.substring(0,line.length()-8));
        }
    }
    
    
    
    
    line = input()
    length = len(line)
    print(line[:length-8])