class Solution:
    longest: int = 0
    
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return -1
            #왼쪽, 오른쪽 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            #가장 긴 경로
            self.longest = max(self.longest, left + right + 2) #거리
            #상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest