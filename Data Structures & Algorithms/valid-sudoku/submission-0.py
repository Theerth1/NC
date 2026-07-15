class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check valdity of each row
        # check validity of each column
        # check validity of each 3x3 box

        
        for row in board:
            rowDict = {}
            for rItem in row:
                if rItem.isdigit() and rItem not in rowDict:
                    rowDict[rItem] = 1
                elif not rItem.isdigit():
                    continue
                else:
                    return False
        

        transpose = zip(*board)
        for row in transpose:
            rowDict = {}
            for rItem in row:
                if rItem.isdigit() and rItem not in rowDict:
                    rowDict[rItem] = 1
                elif not rItem.isdigit():
                    continue
                else:
                    return False

        # 9 lists in a lis
        threes = [[] for i in range(9)]
        for i in range(len(board)):
            if i < 3:
                for j in range(9):
                    if j < 3:
                        if board[i][j].isdigit() and board[i][j] not in threes[0]:
                            threes[0].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
                    elif j < 6:
                        if board[i][j].isdigit() and board[i][j] not in threes[1]:
                            threes[1].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
                    else:
                        if board[i][j].isdigit() and board[i][j] not in threes[2]:
                            threes[2].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
            elif i < 6:
                for j in range(9):
                    if j < 3:
                        if board[i][j].isdigit() and board[i][j] not in threes[3]:
                            threes[3].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
                    elif j < 6:
                        if board[i][j].isdigit() and board[i][j] not in threes[4]:
                            threes[4].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
                    else:
                        if board[i][j].isdigit() and board[i][j] not in threes[5]:
                            threes[5].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
            else:
                for j in range(9):
                    if j < 3:
                        if board[i][j].isdigit() and board[i][j] not in threes[6]:
                            threes[6].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
                    elif j < 6:
                        if board[i][j].isdigit() and board[i][j] not in threes[7]:
                            threes[7].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False
                    else:
                        if board[i][j].isdigit() and board[i][j] not in threes[8]:
                            threes[8].append(board[i][j])
                        elif not board[i][j].isdigit():
                            continue
                        else:
                            return False

        return True


        