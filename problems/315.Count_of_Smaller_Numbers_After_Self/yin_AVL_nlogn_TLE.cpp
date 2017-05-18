// AVL Tree (Self-balancing Binary Search Tree)
// Time Complexity O(nlogn)
// Space Complexity O(n)
// Time Limit Exceeded$: 15 / 16 test cases passed.

// AVL TREE ////////////////////////////
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
	Node *balance(Node *n);
	int height(Node *n) { if (!n) return 0; return max(height(n->left), height(n->right)) + 1; }
	int diff(Node *n) { return height(n->left) - height(n->right); }
	Node *rr_rotation(Node *n); // Right - Right Rotation
	Node *ll_rotation(Node *n); // Left - Left Rotation
	Node *rl_rotation(Node *n); // Right - Left Rotation
	Node *lr_rotation(Node *n); // Left - Right Rotation
public :
	BST() : root(0) { }
	~BST() { if (root) delete root; root = 0; }
	int insert(int val) { 
	    if (!root) { root = new Node(val); return 0; }
	    int res = root->insert(val); 
	    root = balance(root); // balance tree after insertion
	    return res;
	}
};

// Implement rotation and balance functions
Node *BST::balance(Node *n) {
	int fct = diff(n);
	if (fct > 1) {
		if (diff(n->left) > 0) n = rr_rotation(n);
		else n = lr_rotation (n);
	}
	if (fct < -1) {
		if (diff(n->right) > 0) n = rl_rotation(n);
		else n = ll_rotation (n);
	}
	return n;
}
Node *BST::rr_rotation(Node *n) {
	Node *temp = n->left;
	n->left = temp->right;
	// change leftCnt
	if (temp->right) 
	    n->leftCnt = temp->right->leftCnt + temp->right->occur;
	else n->leftCnt = 0;
	temp->right = n;
	return temp;
}
Node *BST::ll_rotation(Node *n) {
	Node *temp = n->right;
	n->right = temp->left;
	temp->left = n;
	// change leftCnt
	temp->leftCnt = n->leftCnt + n->occur;
	return temp;
}
Node *BST::rl_rotation(Node *n) {
	Node *temp = n->right;
	n->right = rr_rotation(temp);
	return ll_rotation(n);
}
Node *BST::lr_rotation(Node *n) {
	Node *temp = ll_rotation(n->left);
	n->left = temp;
	n->leftCnt = temp->leftCnt + temp->occur; // change leftCnt
	return rr_rotation(n);
}

// SOLUTION ///////////////////////////////////////////
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        BST tree; // AVL Tree
        for (int i = n - 1; i >= 0; --i) {
            res[i] = tree.insert(nums[i]);
        }
        return res;
    }
};