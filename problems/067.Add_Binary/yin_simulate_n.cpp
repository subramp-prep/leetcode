class Solution {
public:
    string addBinary(string a, string b)
    {
        string res = "";
        int carry = 0, i = a.size() - 1, j = b.size() - 1;
        while (i >= 0 || j >= 0 || carry)
        {
            int ia = i >= 0 ? a[i] - '0' : 0;
            int ib = j >= 0 ? b[j] - '0' : 0;
            carry += ia + ib;
            res = to_string(carry % 2) + res;
            carry /= 2;
            --i; --j;
        }
        return res;
    }
};