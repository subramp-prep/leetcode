class Solution(object):
    def findSubstring(self, s, words):
        from collections import Counter
        from collections import defaultdict
        c = Counter(words)
        m = len(words)
        n = len(words[0])
        ret = []
        total_length = m * n

        #Loop over word length
        for k in xrange(n):
            left = k
            subd = defaultdict(int)
            count = 0
            #Loop over the string
            for j in xrange(k, len(s) - n + 1, n):
                #Get a word from observed substring
                word = s[j:j+n]
                #check if it is a valid word
                if word in c:
                    subd[word] += 1
                    count += 1
                    ##Shift the window as long as we have encountered more number of a word than is needed
                    ##Note that we can shift the window by word length directly as the outer loop is there to
                    ##make sure that anything is not missed out
                    ##This solution will give indices out of order by OJ accepts it.
                    while subd[word] > c[word]:
                        subd[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    ##Count will be equal to m only when we all the words are read the exact number of times needed
                    if count == m:
                        ret.append(left)
                #If is not a valid word then just skip over the current word (Don't worry about the middle characters
                ##outer loop will take care of it)
                else:
                    left = j + n
                    subd = defaultdict(int)
                    count = 0


        return ret