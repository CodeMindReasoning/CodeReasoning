class main:
    import java.util.ArrayDeque;
    import java.util.HashSet;
    import java.util.Queue;
    import java.util.Scanner;
    import java.util.Set;
    
    class p03212:
        def main(self):
            sc = Scanner(System.in);
            set = HashSet();
            N = sc.nextInt();
            main = p03212();
            queue = ArrayDeque();
            count = 0;
            ch = ['3','5','7'];
            queue.add("357");
            queue.add("375");
            queue.add("537");
            queue.add("573");
            queue.add("735");
            queue.add("753");
            if N<1000:
                for s in queue:
                    if Long.parseLong(s)<=N:
                        count ++;
                System.out.println(count);
                return ;
            while queue.size()>0:
                s = queue.poll();
                if Long.parseLong(s)<=N:
                    count ++;
                    for i in range(0,s.length()):
                        for j in range(0,ch.length):
                            temp = main.addChar(s, i, ch[j]);
                            if set.contains(temp)==false:
                                set.add(temp);
                                queue.add(temp);
                }
            System.out.println(count);
        def addChar(self,s,location,c):
            sb = StringBuffer();
            sb.append(s.substring(0,location));
            sb.append(c);
            if location<s.length():
                sb.append(s.substring(location));
            return sb.toString();
    
    p03212().main();