class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(list)
        column_dict = defaultdict(list)
        square_dict = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                elif board[i][j] in row_dict[i] or board[i][j] in column_dict[j]:
                    return False
                else:
                    row_dict[i].append(board[i][j])
                    column_dict[j].append(board[i][j])
        for i in range(len(board)-2):
            for j in range(len(board)-2):
                if i%3==0 and j%3==0:
                    for k in range(i,i+3):
                        for h in range(j,j+3):
                            if board[k][h] == '.':
                                continue
                            elif board[k][h] in square_dict[i,j]:
                                return False
                            else:    
                                square_dict[i,j].add(board[k][h])
                
        return True