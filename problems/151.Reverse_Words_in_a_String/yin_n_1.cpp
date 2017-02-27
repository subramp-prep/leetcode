void reverseWords(char *s)
{
    int i = 0, cur = 0, cnt = 0, word_cnt = 0;
    
	// remove spaces and reverse each word
    while (true)
    {
        while (s[i] == ' ') ++i; // reach the beginning of the current word
        if (s[i] == '\0') break;
        if (word_cnt++) s[cur++] = ' '; // add space between words
        
        cnt = 0;
        while (s[i + cnt] != '\0' && s[i + cnt] != ' ')
        {
            s[cur + cnt] = s[i + cnt]; // shift word to remove spaces
            ++cnt; // count word length
        }
        
        // reverse current word
        reverse(s + cur, cnt);
        
        // update
        i += cnt;
        cur += cnt;
    }
    s[cur] = '\0'; // cut
    
    // reverse the whole string
    reverse(s, cur);
}

void reverse(char *s, int len)
{
    for (int i = 0; i < len / 2; ++i)
    {
        char tmp = s[i];
        s[i] = s[len - i - 1];
        s[len - i - 1] = tmp;
    }
}