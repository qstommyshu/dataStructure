package java;
import java.util.*;

public class checkParentheses {
    public static void main(String[] args) {
        System.out.println(isValid("(]"));
        
    }
        public static boolean isValid(String s) {
        Stack<Character> container = new Stack<>();
        for(int i=0;i<s.length()-1;i++) {
            if (s.charAt(i) == '('){
                container.push(')');
            }
            if (s.charAt(i) == '['){
                container.push(']');
            }
            if (s.charAt(i) == '{'){
                container.push('}');
            }
            if (s.charAt(i) == ')')
                if(container.pop() != ')'){
                    return false;
                }
            if (s.charAt(i) == ']')
                if(container.pop() != ']'){
                    return false;
                }
            if (s.charAt(i) == '}')
                if(container.pop() != '}'){
                    return false;
                }
        }
        return true;
    }
}

