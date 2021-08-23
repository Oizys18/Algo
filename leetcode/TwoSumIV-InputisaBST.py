# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
answer = 0
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        global answer
        items = []
        answer = 0
        def check(node):
            global answer
            if answer:
                return 
            if node.val in items:
                answer = True
            items.append(k-node.val)
            if node.left:
                check(node.left )
            if node.right:
                check(node.right)
            
        check(root)

        return answer


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        global answer
        items = []
        answer = 0
        def check(node):
            global answer
            if answer:
                return 
            if node.val in items:
                answer = True
            items.append(k-node.val)
            if node.left:
                check(node.left )
            if node.right:
                check(node.right)
            
        check(root)

        return answer


"""
# 처음에 set을 생각했는데, 값이 같은 노드가 2개가 겹치면 (4+4=8) set에 하나밖에 계산안될줄 알고 리스트로 바꿨다. 
근데 지금 다시 보니까 매번 값을 비교하니까 set여도 상관없었다..! 
그리고 재귀로 안하고 while로 돌리는게 더 빠른가봄 

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s=set()
        q=[root]
        while q:
            root = q.pop(0)
            if k-root.val in s:
                return True
            s.add(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return False
"""