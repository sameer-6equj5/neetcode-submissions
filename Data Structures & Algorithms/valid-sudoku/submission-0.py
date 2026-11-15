class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d={}
        for i in range(9):
            row_set=set()
            col_set=set()
            for j in range(9):
                x=board[i][j]
                if x in col_set:
                    return False
                elif x!='.':
                    col_set.add(x)

                y=board[j][i]
                if y in row_set:
                    return False
                elif y!='.':
                    row_set.add(y)

                if (i//3,j//3) not in d:
                    d[(i//3,j//3)]=set()
                    
                if x in d[(i//3,j//3)]:
                    return False
                elif x!='.':
                    d[(i//3,j//3)].add(x)

        
        return True

        