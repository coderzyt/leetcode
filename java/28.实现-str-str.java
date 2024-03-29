/*
 * @lc app=leetcode.cn id=28 lang=java
 *
 * [28] 实现 strStr()
 *
 * https://leetcode-cn.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (39.59%)
 * Likes:    622
 * Dislikes: 0
 * Total Accepted:    257.4K
 * Total Submissions: 650.2K
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 * 
 * 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
 * (从0开始)。如果不存在，则返回  -1。
 * 
 * 示例 1:
 * 
 * 输入: haystack = "hello", needle = "ll"
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 输入: haystack = "aaaaa", needle = "bba"
 * 输出: -1
 * 
 * 
 * 说明:
 * 
 * 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 * 
 * 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
 * 
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {

        if (haystack == null || needle == null) {
            return 0;
        }

        int hlength = haystack.length();
        int nlength = needle.length();

        if (nlength == 0) {
            return 0;
        }

        if (nlength > hlength) {
            return -1;
        }

        int max = hlength - nlength;

        int fromIndex = 0;

        char first = needle.charAt(0);

        for (int i = fromIndex; i <= max; i++) {
            
            if (haystack.charAt(i) != first) {
                while (++i <= max && haystack.charAt(i) != first);
            }

            if (i <= max) {
                int j = i + 1;
                int end = j + nlength - 1;
                for (int k = 1; j < end && haystack.charAt(j) == needle.charAt(k); j++, k++);
                if (j == end) {
                    return i;
                }
            }
        }
        return -1;
    }
}
// @lc code=end

