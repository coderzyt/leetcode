package Offer;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {

        if (head == null) {
            return new int[0];
        }

        Stack<Integer> stack = new Stack<Integer>();

        ListNode node = head;

        stack.push(node.val);
        while (node.next != null) {
            stack.push(node.next.val);
            node = node.next;
        }

        int size = stack.size();

        int[] result = new int[size];

        for (int i = 0; i < result.length; i++) {
            result[i] = stack.pop();
        }

        return result;
    }

    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || preorder.length == 0) {
            return null;
        }
        int length = preorder.length;
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < length; i++) {
            indexMap.put(inorder[i], i);
        }
        TreeNode root = buildTree(preorder, 0, length - 1, inorder, 0, length - 1, indexMap);
        return root;
    }

    public TreeNode buildTree(int[] preorder, int preorderStart, int preorderEnd, 
    int[] inorder, int inorderStart, int inorderEnd, HashMap<Integer, Integer> indexMap) {

        if (preorderStart > preorderEnd) {
            return null;
        }
        int rootVal = preorder[preorderStart];

        TreeNode root = new TreeNode(rootVal);

        if (preorderStart == preorderEnd) {
            return root;
        } else {
            int rootIndex = indexMap.get(rootVal);
            int leftNodes = rootIndex - inorderStart, rightNodes = inorderEnd - rootIndex;
            TreeNode leftSubTree = buildTree(preorder, preorderStart + 1, preorderStart + leftNodes, inorder, inorderStart, rootIndex - 1, indexMap);
            TreeNode rightSubTree = buildTree(preorder, preorderEnd - rightNodes + 1, preorderEnd, inorder, rootIndex + 1, inorderEnd, indexMap);
            root.left = leftSubTree;
            root.right = rightSubTree;
            return root;
        }
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }



 
}

