def judgePoint24(self, nums):
    bad = '떢븻각걎냇갅갸꺚뵟숣욄뵴뵞뤼갈갌뤔떌옊메늄숭캸긶꺛옖갍뇐쩢곴듇걯궄옕왹눞솴걃끗긬땉궿가쌀낐걄숤뺴늘걘꽸숢걂갋갃쫐꼔솾쩡쇔솿끛뤜간븺쩬웨딴옠뤛갂뵪덠놤빐옋귒늂갰갖놥궾갆옌뼘묰거갎긷낤겼'
    return chr(int(''.join(map(str, sorted(nums)))) + 42921) not in bad


# There are really only 495 possible inputs, of which 404 are solvable and
# 91 aren't. The above is the shortest encoding of those 91 that I could
# think of. One character for each case. The +42921 is for getting all
# characters from the same unicode range (from the "Hangul Syllables"
# range) so that it looks good. For extra style points I shuffled them,
# otherwise they'd look somewhat sorted.

# I helped preparing the problem for the contest. For that, I tested
# solutions on all inputs. That's where I realized there aren't that many.
# And the solutions took about two minutes for all inputs, I think that's
# where I thought about pre-computing. Partly because I wanted a fast
# solution to easily compare other solutions against.

# And then I just had fun making it small. I like doing things differently
# and coming up with stuff people don't usually think of. In the end I was
# a bit inspired by people occasionally posting here in Chinese or so. At
# least that's why I used the string as my title, just a little joke.
