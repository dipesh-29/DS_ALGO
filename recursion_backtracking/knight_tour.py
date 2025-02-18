'''
def knight_tour(chess_board,i,j,n,count):
    if i >= n or j >= n or i < 0 or j < 0 or chess_board[i][j]!=0:
        return
    if chess_board[i][j] == 0:
        chess_board[i][j] = count
    elif count == n*n-1:
        return
    knight_tour(chess_board,i+2,j+1,n,count+1)
    knight_tour(chess_board,i+2,j-1,n,count+1)
    knight_tour(chess_board,i-2,j+1,n,count+1)
    knight_tour(chess_board,i-2,j-1,n,count+1)
    knight_tour(chess_board,i+1,j+2,n,count+1)
    knight_tour(chess_board,i-1,j+2,n,count+1)
    knight_tour(chess_board,i+1,j-2,n,count+1)
    knight_tour(chess_board,i-1,j-2,n,count+1)
    return chess_board
    #chess_board[i][j] = 0





if __name__ == '__main__':
    n = 4
    chess_board = [[0 for _ in range(n)] for _ in range(n)]
    knight_tour(chess_board,0,0,n,0)
    print(chess_board)
'''

n = 5
def isSafe(x,y,board):

  if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
    return True
  return False

def printSolution(board):

  for i in range(n):
    print(board[i])

def solveKT():
  board = [[-1 for i in range(n)]for i in range(n)]


  move_x = [2, 1, -1, -2, -2, -1, 1, 2]
  move_y = [1, 2, 2, 1, -1, -2, -2, -1]


  board[0][0] = 0


  pos = 1

  if(not solveKTUtil(board, 0, 0, move_x, move_y, pos)):
    print("Solution does not exist")
  else:
    printSolution(board)
def solveKTUtil(board,curr_x,curr_y,move_x,move_y,pos):


  if(pos == n**2):
    return True


  for i in range(8):
    new_x = curr_x + move_x[i]
    new_y = curr_y + move_y[i]
    if(isSafe(new_x,new_y,board)):
      board[new_x][new_y] = pos
      if(solveKTUtil(board,new_x,new_y,move_x,move_y,pos+1)):
        return True


      board[new_x][new_y] = -1
  return False

if __name__ == "__main__":
  solveKT()
