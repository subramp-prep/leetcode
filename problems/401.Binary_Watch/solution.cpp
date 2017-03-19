vector<string> readBinaryWatch(int num) {
    vector<string> rs;
    for (int h = 0; h < 12; h++)
    for (int m = 0; m < 60; m++)
        if (bitset<10>(h << 6 | m).count() == num)
            rs.emplace_back(to_string(h) + (m < 10 ? ":0" : ":") + to_string(m));
    return rs;
}

//emplace_back 添加一个新元素到容器的结尾。
//这个元素会直接在容器结尾构造，即没有复制或移动操作进行。