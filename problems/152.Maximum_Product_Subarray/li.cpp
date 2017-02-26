class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        int big = 0, small = 0;// 累积计算值
        int big2, small2;// 计算中间过渡值
        int result = 0;// 动态结果

        for(int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                big = max(nums[i], nums[i] * big); // 必须取nums[i]，big为0也没关系
                small = nums[i] * small; // 必须取nums[i]，small为0也没关系
            } else if (nums[i] < 0){
                big2 = nums[i] * small; // 必须取nums[i]，small为0也没关系
                small2 = min(nums[i], nums[i] * big); // 必须取nums[i]，big为0也没关系
                small = small2;
                big = big2;
            } else {
                small = big = 0; //nums[i]为0，big和small重置，分第三类为了更清楚
            }
            result = max(result, big); //更新当前找到的最佳动态结果
        }
        return result;
    }
};