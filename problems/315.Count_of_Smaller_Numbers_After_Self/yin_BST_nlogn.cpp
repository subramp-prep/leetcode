// Binary Search Tree
// Time Complexity O(n^2) θ(nlogn)
// Space Complexity O(n)
// BST ////////////////////////////
struct Node {
    int val;
    int occur;
    int leftCnt;
    Node *left;
    Node *right;
    
    // constructor, destructor
    Node(int x) : val(x), occur(1), leftCnt(0), left(0), right(0){ }
    ~Node() { delete left; left = 0; delete right; right = 0; }
    
    // insert
    int insert(int x) {
        if (x == val) {
            ++occur;
            return leftCnt;
        } else if (x < val) {
            ++leftCnt;
            if (!left) {
                left = new Node(x);
                return 0;
            } else return left->insert(x);
        } else {
            if (!right) {
                right = new Node(x);
                return leftCnt + occur;
            } else return leftCnt + occur + right->insert(x);
        }
        return -1;
    }
};
    
class BST {
private :
	Node *root;

public :
	BST() : root(0) { }
	~BST() { if (root) delete root; root = 0; }
	int insert(int val) { 
	    if (!root) { root = new Node(val); return 0; }
	    int res = root->insert(val); 
	    return res;
	}
};

// SOLUTION ///////////////////////////////////////////
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        BST tree; // BST
        for (int i = n - 1; i >= 0; --i) {
            res[i] = tree.insert(nums[i]);
        }
        return res;
    }
};