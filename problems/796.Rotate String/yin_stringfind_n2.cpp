// Time complexity O(n2)
// Space complexity O(1)
class Solution {
public:
    bool rotateString(string A, string B) {
        // corner case
        if (A.size() != B.size())
            return false;
        
		// concatenate 2 As and search B in it 
        return (A + A).find(B) != string::npos;
    }
};

// The time complexity of this algo should be that of string::find(), in most cases it's O(N*M)