# coding:utf-8
import os
import time

strs = [
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy0',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy1',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy2',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy3',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy4',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy5',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy6',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy7',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy8',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy9',
    '1234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy01234567890abcdefghijklmnopqrstuvwxy10'
]


def test1(strs):
    if not strs:
        return ""
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


def test2(strs):
    return os.path.commonprefix(strs)


def test3(strs):
    if not strs:
        return ""
    res = strs[0]
    for str in strs:
        while res and str[:len(res)] != res:
            res = res[:-1]
    return res


def test4(strs):
    if not strs:
        return ""
    strs.sort()
    s1, s2 = strs[0], strs[-1]
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1


def test5(strs):
    if not strs:
        return ""
    res = strs[0]
    for str in strs:
        j = 0
        while j < len(res) and j < len(str) and res[j] == str[j]:
            j += 1
    return res


N = 10000
start = time.time()
for _ in range(N):
    test1(strs)
print "set", time.time() - start

start = time.time()
for _ in range(N):
    test2(strs)
print "os:", time.time() - start

start = time.time()
for _ in range(N):
    test3(strs)
print "Jerrold:", time.time() - start

start = time.time()
for _ in range(N):
    test4(strs)
print "Sort by Han", time.time() - start

start = time.time()
for _ in range(N):
    test5(strs)
print "今日最佳", time.time() - start
