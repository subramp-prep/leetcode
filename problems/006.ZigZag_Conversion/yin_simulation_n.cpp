class Solution
{
    // Simulate zigzag procedure
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1)
            return s;
        
        string *strRows = new string[numRows];
        
        int row = 0, direct = 1;
        for (int i = 0; i < s.size(); ++i)
        {
            strRows[row].push_back(s[i]);
            
            // Going down
            if (row == 0)
                direct = 1;
                
            // Going up
            if (row == numRows - 1)
                direct = -1;
                
            // next row
            row += direct;
        }
        
        // append strings
        s.clear();
        for (int i = 0; i < numRows; ++i)
        {
            s.append(strRows[i]);
        }
        
        // clean
        delete[] strRows;
        
        // return
        return s;
    }
};