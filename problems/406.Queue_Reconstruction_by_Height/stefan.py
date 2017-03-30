def reconstructQueue(self, people):
    people.sort(key=lambda (h, k): (-h, k))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue


def reconstructQueue(self, people):
    return reduce(lambda q, p: q.insert(p[1], p) or q, sorted(people, key=lambda (h, t): (-h, t)), [])


# https://discuss.leetcode.com/topic/60981/explanation-of-the-neat-sort-insert-solution
