class Solution(object):

    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        i = code.find('>')
        if i < 0:
            return False
        tag = code[1:i]
        for c in tag:
            if not 'A' <= c <= 'Z':
                return False
        if code[0] != '>' or not code.endswith('</' + tag + '>'):
            return False
