def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()


return word in [word.upper(), word.lower(), word.capitalize()]