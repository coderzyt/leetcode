import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 *
 * https://leetcode-cn.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (43.26%)
 * Likes:    1985
 * Dislikes: 0
 * Total Accepted:    458.4K
 * Total Submissions: 1.1M
 * Testcase Example:  '"()"'
 *
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
 * 
 * 有效字符串需满足：
 * 
 * 
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 * 
 * 
 * 注意空字符串可被认为是有效字符串。
 * 
 * 示例 1:
 * 
 * 输入: "()"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: "()[]{}"
 * 输出: true
 * 
 * 
 * 示例 3:
 * 
 * 输入: "(]"
 * 输出: false
 * 
 * 
 * 示例 4:
 * 
 * 输入: "([)]"
 * 输出: false
 * 
 * 
 * 示例 5:
 * 
 * 输入: "{[]}"
 * 输出: true
 * 
 */

// @lc code=start
class Solution {

    public static final Map<Character, Character> map = new HashMap<Character, Character>(){{
        put('(', ')');
        put('[', ']');
        put('{', '}');
        put('?', '?');
    }};
    
    public boolean isValid(String s) {

        if (s == null || s.length() == 0) {
            return false;
        }

        int n = s.length();
        if (n % 2 == 1) {
            return false;
        }

        if (n > 0 && !map.containsKey(s.charAt(0))) {
            return false;
        }

        char[] chars = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        stack.push('?');
        for (char c : chars) {
            if (map.containsKey(c)) {
                stack.push(c);
            } else if (map.get(stack.pop()) != c) {
                return false;
            }
        }
        return stack.size() == 1;
    }
}
// @lc code=end

