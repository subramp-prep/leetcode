// Time Complexity O(n^2)
// Space Complexity O(1)
class Solution {
public:
    bool rotateString(string A, string B) {
        // corner case
        if (A.size() != B.size())
            return false;
        
        int n = A.size();
        for (int i = 0; i < n; ++i)
        {
            //match first letter of B in A
            if (A[i] == B[0])
            {
                bool match = true;
                for (int j = 0; i + j < n; ++j)
                {
                    // match right side
                    if (A[i + j] != B [j])
                    {
                        match = false;
                        break;
                    }
                    // match left side
                    if (j < i && A[j] != B[n - i + j])
                    {
                        match = false;
                        break;
                    }
                }
                // if unmatched, redo the match
                if (!match)
                    continue;
                else
                    return true;
            }
        }
        return false;
    }
};

//////////////////////////////////////////////////////////////
// Time Complexity O(n^2)
// Space Complexity O(1)
class Solution {
public:
    bool rotateString(string A, string B) {
        // corner case
        if (A.size() != B.size())
            return false;
        
        for (int i = 0; i < A.size(); ++i)
        {
			// rotate string and compare
            A = (A + A[0]).substr(1);
            if (A == B)
                return true;
        }
        return false;
    }
};