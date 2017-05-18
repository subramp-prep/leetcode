// Binary Search Tree
// Time Complexity O(n^2)，θ(nlogn)
// Space Complexity O(n)

// TREE NODE ////////////////////////////
struct Node {
    long long val;
    int cnt; // occurrence of current value
    int leftcnt; // number of nodes on its left subtree
    Node *left, *right;
    
    Node(long long v) : val(v), cnt(1), leftcnt(0), left(0), right(0) {};
    ~Node() {if (left) delete left; if (right) delete right; left = right = 0; };
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

// BST ////////////////////////////
class BST {
private:
    int upper;
    int lower;
    Node *root;
public:
    BST(int u, int l) : upper(u), lower(l), root(new Node(0)) {};
    ~BST(){delete root; root = 0;}
    int insert_count(long long val) {
        int res = root->getBound(val - lower, true) - root->getBound(val - upper, false);
        root->insert(val);
        return res;
    };
};

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