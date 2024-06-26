class main:
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStream;
    import java.io.InputStreamReader;
    import java.io.OutputStream;
    import java.io.PrintWriter;
    import java.util.InputMismatchException;
    import java.util.StringTokenizer;
    
    public class p03291 {
    
        public static void main(String[] args) throws IOException {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            InputReader in = new InputReader(inputStream);
            PrintWriter out = new PrintWriter(outputStream);
            TaskX solver = new TaskX();
            solver.solve(1, in, out);
            out.close();
        }
    
        static int INF = 1 << 30;
        static long LINF = 1L << 55;
        static int MOD = 1000000007;
        static int[] mh4 = { 0, -1, 1, 0 };
        static int[] mw4 = { -1, 0, 0, 1 };
        static int[] mh8 = { -1, -1, -1, 0, 0, 1, 1, 1 };
        static int[] mw8 = { -1, 0, 1, -1, 1, -1, 0, 1 };
    
        static class TaskX {
    
            public void solve(int testNumber, InputReader in, PrintWriter out) {
    
                char[] s = in.nextString().toCharArray();
                int n = s.length;
                long[] ac = new long[n+1];
                long[] bc = new long[n+1];
                long[] cc = new long[n+1];
                long[] xc = new long[n+1];
                for (int i = 0; i < n; i++) {
                    ac[i+1] += ac[i];
                    bc[i+1] += bc[i];
                    cc[i+1] += cc[i];
                    xc[i+1] += xc[i];
                    if (s[i] == 'A') ac[i+1]++;
                    if (s[i] == 'B') bc[i+1]++;
                    if (s[i] == 'C') cc[i+1]++;
                    if (s[i] == '?') xc[i+1]++;
                }
    
                long ans =