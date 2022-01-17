class Solution {
public:
    bool chk_cycle(vector<vector<char>>&grid,vector<vector<int>>&vstd,int row,int col,int par)
    {
        if(vstd[row][col]+1==par)
        {
            return 0;
        }
        else if(vstd[row][col]+1!=par)
        {
            return 1;
        }
        vstd[row][col]=par+1;
        if(row+1<grid.size() && grid[row+1][col]==grid[row][col])
        {
            if(chk_cycle(grid,vstd,row+1,col,vstd[row][col]))
            {
                return 1;
            }
        }
        if(row-1>=0 && grid[row-1][col]==grid[row][col])
        {
            if(chk_cycle(grid,vstd,row-1,col,vstd[row][col]))
            {
                return 1;
            }
        }
        if(col+1<grid[0].size() && grid[row][col+1]==grid[row][col])
        {
            if(chk_cycle(grid,vstd,row,col+1,vstd[row][col]))
            {
                return 1;
            }
        }
        if(col-1>=0 && grid[row][col-1]==grid[row][col])
        {
            if(chk_cycle(grid,vstd,row,col-1,vstd[row][col]))
            {
                return 1;
            }
        }
        vstd[row][col]=0;
     return 0;   
    }
    bool containsCycle(vector<vector<char>>& grid) {
        vector<vector<int>>vstd(grid.size(),vector<int>(grid[0].size(),0));
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[i].size();j++)
            {
                if(chk_cycle(grid,vstd,i,j,0))
                {
                    return 1;
                }
            }
        }
        return 0;
    }
};