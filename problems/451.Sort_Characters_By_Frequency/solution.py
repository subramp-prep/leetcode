class Solution(object):

    def frequencySort(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([c * frq for c, frq in collections.Counter(str).most_common()])

# https://discuss.leetcode.com/topic/65861/1-line-python-code


# By using heqpq.nlargest
# h = [(v, k) for k, v in Counter(s).items()]
#     return ''.join(v * k for v, k in heapq.nlargest(len(h), h))
