class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(x,y):
            for i in range(9):
                if i!=x:
                    if (board[i][y] != '.') and (board[i][y]== board[x][y]):
                        return False 
                if i!=y:
                    if (board[x][i] != '.') and (board[x][i] == board[x][y]):
                        return False 
            nx,ny = (x//3)*3, (y//3)*3
            for a in range(3):
                for b in range(3):
                    if nx+a != x and ny+b != y:
                        if (board[nx+a][ny+b]!= '.') and (board[nx+a][ny+b] == board[x][y]):
                            return False        
            return True 
        
        for x in range(9):
            for y in range(9):
                if board[x][y] !='.':
                    if not check(x,y):
                        return False 
        return True 