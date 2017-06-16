def addBoldTag(self, s, dict):
    bold = [False] * len(s)
    for i in range(len(s)):
        length = max([len(word)
                      for word in dict
                      if s.startswith(word, i)] or [0])
        bold[i:i + length] = [True] * length
    it = iter(s)
    return ''.join('<b>' * k + ''.join(itertools.islice(it, len(list(g)))) + '</b>' * k
                   for k, g in itertools.groupby(bold))


def addBoldTag(self, s, dict):
    def bold():
        end = 0
        for i in range(len(s)):
            for word in dict:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            yield end > i
    it = iter(s)
    return ''.join('<b>' * k + ''.join(itertools.islice(it, len(list(g)))) + '</b>' * k
                   for k, g in itertools.groupby(bold()))
