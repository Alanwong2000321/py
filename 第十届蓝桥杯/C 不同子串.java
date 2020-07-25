import java.util.*;

public class Main {
    public static void main(String[] args) {
        String s ="0100110001010001";
        Set<String> set = new HashSet<String>();       //Set最大的特点就是不能存重复的元素
        for (int i = 0; i < s.length(); i++) {                   //for循环每一种可能，加入set里面
            for (int j = i+1; j <= s.length(); j++) {
                String a = s.substring(i,j);
                set.add(a);
            }
        }
        System.out.println(set.size());
    }
        }