/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */
object Solution {
    def getMinimumDifference(root: TreeNode): Int = {
        var min=Int.MaxValue;
        var pre=null
        def inOrder(root:TreeNode):Unit={
            if (Option(root).nonEmpty){
                inOrder(root.left);
                if (pre!=null)
                    min=Math.min(min,Math.abs(pre.value-root.value));
                pre=root;
                inOrder(root.right)
            }
        }
        inOrder(root);
        min

    }
}

/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */
object Solution {
    def getMinimumDifference(root: TreeNode): Int = {
         var pre:TreeNode = null;
  var min:Int = Int.MaxValue;
//中序遍历
  def minDiffInBST(root: TreeNode): Int = {
    middleOrderTraverse(root);
     min;
  }

  def middleOrderTraverse(root: TreeNode):Unit  = {
    if(Option(root).isEmpty) return;
    middleOrderTraverse(root.left);
    if(pre != null){
        min=Math.min(min,Math.abs(root.value -pre.value))
    }
    pre =root;
    middleOrderTraverse(root.right);
  }
  minDiffInBST(root)
    }
}