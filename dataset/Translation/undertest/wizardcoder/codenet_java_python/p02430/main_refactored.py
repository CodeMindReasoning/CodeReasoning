class main:
    import java.util.*;
    import java.io.*;
    
    public class p02430 {
    
    	void solve (FastScanner in, PrintWriter out, Methods ms) {
    		
    		int n = in.nextInt(), k = in.nextInt();
    		
    		for (int bit=0; bit<(1<<n); bit++) {
    			if (Integer.bitCount(bit)!= k) continue;
    			out.print(bit+":");
    			for (int j=0; j<n; j++) {
    				if (((bit>>j) & 1) == 1) {
    					out.print(" "+j);
    				}
    			}
    			out.println();
    		}
    		
    	}
    
    	public static void main(String[] args) {
    		p02430 main = new p02430();
    		FastScanner in = new FastScanner(System.in);
    		PrintWriter out = new PrintWriter(System.out);
    		Methods ms = new Methods();
    		main.solve(in, out, ms);
    		in.close();
    		out.close();
    	}
    
    	static class Methods {
    
    		public void print (Object... ar) {System.out.println(Arrays.deepToString(ar));}
    
    		public void yesno (PrintWriter out, boolean b) {out.println(b?"Yes":"No");}
    
    		public void YESNO (PrintWriter out, boolean b) {out.println(b?"YES":"NO");}
    
    		public int max (int... ar) {Arrays.sort(ar); return ar[ar.length-1];}
    
    		public int min (int... ar) {Arrays.sort(ar); return ar[0];}
    
    	}
    
    	static class FastScanner {
    
    		private InputStream in;
    		private byte[] buffer = new byte[1024];
    		private  int length = 0, p = 0;
    
    		public FastScanner (InputStream stream) {
    			in = stream;
    		}
    
    		public boolean hasNextByte () {
    			if (p < length) return true;
    			else {
    				p = 0;
    				try {length = in.read(buffer);}
    				catch (Exception e) {e.printStackTrace();}
    				if (length <= 0) return false;
    			}
    			return true;
    		}
    
    		public int readByte () {
    			if (hasNextByte() == true) return buffer[p++];
    			return -1;
    		}
    
    		public boolean isPrintable (int n) {return 33<=n&&n<=126;}
    
    		public void skip () {
    			while (hasNextByte() &&!isPrintable(buffer[p])) p++;
    		}
    
    		public boolean hasNext () {skip(); return hasNextByte();}
    
    		public String next () {
    			if (!hasNext()) throw new NoSuchElementException();
    			StringBuilder sb = new StringBuilder();
    			int t = readByte();
    			while (isPrintable(t)) {
    				sb.appendCodePoint(t);
    				t = readByte();
    			}
    			return sb.toString();
    		}
    
    		public String[] nextArray (int n) {
    			String[] ar = new String[n];