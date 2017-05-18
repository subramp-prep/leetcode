// AVL Self Search Tree
// Time Complexity O(nlogn)
// Space Complexity O(n)
// Time Limit Exceeded: 61 / 61 test cases passed

// TREE NODE ////////////////////////////
struct Node {
    long long val;
    int cnt; // occurrence of current value
    int leftcnt; // number of nodes on its left subtree
    Node *left, *right;
    
    Node(long long v) : val(v), cnt(1), leftcnt(0), left(0), right(0) {};
    ~Node() {if (left) delete left; if (right) delete right; left = right = 0; };
    int count() { return cnt + leftcnt + (right ? right->count() : 0); }
    void insert(long long x) {
        if (x == val) {
            ++cnt;
        } else if (x < val) {
            ++leftcnt;
            if (!left) left = new Node(x);
            else left->insert(x);
        } else {
            if (!right) right = new Node(x);
            else right->insert(x);
        }
    }
    
    int getBound(long long x, bool self)
    {
        if(val == x) return  leftcnt + (self ? cnt : 0);
        else if(val > x) return left ? left->getBound(x, self) : 0;
        else return cnt + leftcnt + (right ? right->getBound(x, self) : 0);
    }
};

// AVL TREE ////////////////////////////
class BST {
private:
    int upper;
    int lower;
    Node *root;
    Node *balance(Node *n);
	int height(Node *n) { if (!n) return 0; return max(height(n->left), height(n->right)) + 1; }
	int diff(Node *n) { return height(n->left) - height(n->right); }
	Node *rr_rotation(Node *n); // Right - Right Rotation
	Node *ll_rotation(Node *n); // Left - Left Rotation
	Node *rl_rotation(Node *n); // Right - Left Rotation
	Node *lr_rotation(Node *n); // Left - Right Rotation
public:
    BST(int u, int l) : upper(u), lower(l), root(new Node(0)) {};
    ~BST(){delete root; root = 0;}
    int insert_count(long long val) {
        int res = root->getBound(val - lower, true) - root->getBound(val - upper, false);
        root->insert(val);
        root = balance(root);
        return res >= 0 ? res : 0;
    };
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
	// change leftcnt
	if (temp->right) 
	    n->leftcnt = temp->right->count();
	else n->leftcnt = 0;
	temp->right = n;
	return temp;
}
Node *BST::ll_rotation(Node *n) {
	Node *temp = n->right;
	n->right = temp->left;
	temp->left = n;
	// change leftcnt
	temp->leftcnt += n->leftcnt + n->cnt;
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
	// change leftcnt
	n->leftcnt = temp->leftcnt + temp->cnt;
	return rr_rotation(n);
}

// SOLUTION ////////////////////////////
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        BST tree(upper, lower);
        int res = 0;
        long long sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            res += tree.insert_count(sum);
        }
        return res;
    }
};