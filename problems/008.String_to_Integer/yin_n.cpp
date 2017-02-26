class Solution {
public:
    int myAtoi(string str)
    {
        int multi = 1, i = 0;
        long res = 0;
        
        while (str[i] == ' ')
            ++i;
        
        if (str[i] == '-' || str[i] == '+')
        {
            if (str[i] == '-') multi = -1;
            ++i;
        }
        
        while (i < str.size() && str[i] >= '0' && str[i] <= '9')
        {
            res = res * 10 + (str[i++] - '0');
            if (res * multi > INT_MAX) return INT_MAX;
            if (res * multi < INT_MIN) return INT_MIN;
        }
        
        return res * multi;
    }
};