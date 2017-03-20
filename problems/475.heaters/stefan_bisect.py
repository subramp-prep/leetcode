def findRadius(self, houses, heaters):
    heaters.sort()
    return max(min(abs(house - heater)
                   for i in [bisect.bisect(heaters, house)]
                   for heater in heaters[i - (i > 0):i + 1])
               for house in houses)
