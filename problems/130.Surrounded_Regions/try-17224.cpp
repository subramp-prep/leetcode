class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int i,j;
        int row=board.size();
        if(!row) return;
        int col=board[0].size();
        if (min(col,row) <= 2) return;
        for(i=0;i<row;i++){
            check(board,i,0,row,col);
            check(board,i,col-1,row,col);
        }
        for(j=0;j<col;j++){
            check(board,0,j,row,col);
            check(board,row-1,j,row,col);
        }
        for(i=0;i<row;i++) for(j=0;j<col;j++) {
            board[i][j] = (board[i][j] == '1') ? 'O' : 'X';
        }

    }
    void check(vector<vector<char> >&vec,int i,int j,int row,int col){
        if(i>=0 && i<row && j>=0 && j<col && vec[i][j]=='O'){
            vec[i][j]='1';
            check(vec,i+1,j,row,col);
            check(vec,i,j+1,row,col);
            check(vec,i-1,j,row,col);
            check(vec,i,j-1,row,col);
        }
    }
};

//runtime error, stack overflow during dfs