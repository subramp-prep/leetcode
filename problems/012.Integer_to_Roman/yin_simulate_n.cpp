class Solution
{
public:
    string intToRoman(int num)
    {
        string res;
        int i = 0; // position of current digit
        
        // Roman numerials are based on seven symbols : I-1, V-5, X-10, L-50, C-100, D-500, M-1000
        char totalSymbols[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        
        while (num > 0)
        {
            // define symbols
            char *symbols = totalSymbols + i * 2;

            // get string for a digit
            int digit = num % 10;
            num = num / 10;
            ++i;
            string temp;
            
           if (digit == 9)
            {
                temp += symbols[0]; // 1symbol
                temp += symbols[2]; // 10symbol
            }
            else if (digit >= 5)
            {
                temp += symbols[1]; // 5symbol
                while (digit > 5)
                {
                    temp += symbols[0]; // 1symbol
                    --digit;
                }
            }
            else if (digit > 3) // 4
            {
                temp += symbols[0]; // 1symbol
                temp += symbols[1]; // 5symbol
            }
            else if (digit > 0)
            {
                while (digit > 0)
                {
                    temp += symbols[0]; // 1symbol
                    --digit;
                }
            }
            
            // append
            res = temp.append(res);
        }
        
        return res;
    };
};