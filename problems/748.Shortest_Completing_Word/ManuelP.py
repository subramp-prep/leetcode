def shortestCompletingWord(self, licensePlate, words):
    counter = Counter(re.sub('[^a-z]', '', licensePlate.lower()))
    return min((word for word in words if not counter - Counter(word)), key=len)
