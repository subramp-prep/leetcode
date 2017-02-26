class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1)
            return s;

        // declare
        int row = 0,       // current row
            j = 0,         // position in current row
            i = 0,         // index in result string
            index = 0,     // index in original string
            size = s.size();
        string res = s; 
        
        while (i < size - 1)
        {
            // we skip the first char as they are always the same
            ++i;
            
            // calculate index
            if (row == 0 || row == numRows - 1)
            {
                index = index + 2 * (numRows - 1);
            }
            else if (j % 2 == 0)
            {
                index = index + 2 * (numRows - row - 1);
            }
            else
            {
                index = index + 2 * row;
            }
            
            // decide whether to change row or not
            if (index >= size)
            {
                ++row;
                index = row;
                j = 0;
            }
            else
            {
                ++j;
            }
            
            res[i] = s[index];
        };

        return res;
    }
};