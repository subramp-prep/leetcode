struct Solution {
    string addBinary(string a, string b) {
        if (a.size() < b.size())
            swap(a, b);
        int i = a.size(), j = b.size();
        while (i--) {
            if (j) a[i] += b[--j] & 1; //char转int 可能位操作效率比较高
            if (a[i] > '1') { //判断需要进位，用char做比较
                a[i] -= 2; //a[i] -= 2;
                if (i) a[i-1]++; else a = '1' + a; //for carry
            }
        }
        return a;
    }
};

// I just write the sum into the longer one of the inputs.
// Don't worry about modifying them,
// as getting string means we're getting copies.
// The "O(1) space" of course refers to the space I use
// in addition to input and output.
// If the output doesn't need to be longer than the longer input,
// I even only use O(1) space in addition to only the input.