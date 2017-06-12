# It does get accepted (in about 90 ms),
# though I'm not entirely sure it's correct `
# because I didn't think it through
# because I don't find the description clear.
# Anyway... first I replace any CDATA with c.
# Then repeatedly replace any tags not containing < with t.
# I return whether I end up with 't'.


def isValid(self, code):
    if code == 't':
        return False
    code = re.sub(r'<!\[CDATA\[.*?\]\]>', 'c', code)
    prev = None
    while code != prev:
        prev = code
        code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
    return code == 't'


# Edit: There is problem of the given string already being "t".
# Fixed now by adding that annoying initial check.


# Edit 2: Here's a version where I handle that problem a different way,
# by also replacing any initial 't' along with any cdata.

def isValid(self, code):
    code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
    prev = None
    while code != prev:
        prev = code
        code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
    return code == 't'
