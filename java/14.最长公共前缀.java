/*
 * @lc app=leetcode.cn id=14 lang=java
 *
 * [14] 最长公共前缀
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        String prefix = strs[0];
        int length = strs.length;

        for (int i = 1; i < length; i++) {
            prefix = this.longestCommonPrefix(prefix, strs[i]);
            if (prefix.equals("")) {
                return "";
            }
        }
        
        return prefix;
    }

    public String longestCommonPrefix(String s1, String s2) {
        int length = Math.min(s1.length(), s2.length());
        int index = 0;
        while (index < length && s1.charAt(index) == s2.charAt(index)) {
            index++;
        }
        return s1.substring(0, index);
    }
}
// @lc code=end

