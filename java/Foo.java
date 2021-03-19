import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Foo {

    public static void main(String[] args) {
        isValid("{}");
    }

    public static boolean isValid(String s) {

        if (s == null || s.length() == 0) {
            return false;
        }
        Map<Character, Integer> map = new HashMap<>();
        map.put('{', -1);
        map.put('}', 1);
        map.put('[', -2);
        map.put(']', 2);
        map.put('{', -3);
        map.put('}', 3);

        char[] chars = s.toCharArray();
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);
        for (char c : chars) {
            int i = map.get(c);
            if (stack.peek() + i == 0) {
                stack.pop();
            } else {
                stack.push(i);
            }
        }

        if (stack.peek() == 0) {
            return true;
        } else {
            return false;
        }
    }

}