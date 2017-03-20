# Go through houses and heaters in ascending order. My i points to the
# current closest heater. Go to the next heater if the current house
# coordinate is larger than or equal to the middle between the current and
# the next heater.


def findRadius(self, houses, heaters):
    heaters = sorted(heaters) + [float('inf')]
    i = r = 0
    for x in sorted(houses):
        while x >= sum(heaters[i:i + 2]) / 2.:
            i += 1
        r = max(r, abs(heaters[i] - x))
    return r

# https://discuss.leetcode.com/topic/71456/short-python
# I btw started with
#     while abs(heaters[i+1] - x) <= abs(heaters[i] - x): ,
# the straight - forward check whether the next heater is closer than the current.
# Then I thought I probably don't need abs if I just use
#     while heaters[i + 1] - x <= x - heaters[i]: .
# That's obviously correct if x is between the heaters,
# because then that's the correct distances of x to the two heaters.
# Less obviously(but imho not surprisingly)
# it's also correct if x isn't between them.
# Finally, after rewriting it to
#     while heaters[i] + heaters[i + 1] <= 2 * x:
# I realized what that meant: -)
