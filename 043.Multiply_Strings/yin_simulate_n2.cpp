class Solution {
public:
    string multiply(string num1, string num2)
    {
		// two numbers can be seen as polynomes of base 10
		// for example, 456 = 4*100 + 5 * 10 + 6 * 1
		// hence, we can apply formula of polynomial multiplication here
        if (num1 == "0" || num2 == "0") return "0";
        
        int l1 = num1.size(), l2 = num2.size(), carry = 0;
        string res = "";
		// with no leading zero, result should have (l1 + l2 - 1) or (l1 + l2) digits
        for (int i = 0; i < l1 + l2 - 1; ++i) // calculate digit by digit backwards
        {
            for (int j = 0; j <= i; ++j)
                if (j < l1 && i - j < l2)
                    carry += (num1[l1 - j - 1] - '0') * (num2[l2 - i + j - 1] - '0');
            
            res = to_string(carry % 10) + res;
            carry = carry / 10;
        }
        
        if (carry)
            res = to_string(carry) + res;
		
        return res;
    }
};