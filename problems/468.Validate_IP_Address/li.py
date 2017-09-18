class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def isIPv4(s):
            s = s.split('.')
            return len(s) == 4 and all(isIPv4_part(i) for i in s)


        def isIPv4_part(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False

        def isIPv6(s):
            s = s.split(':')
            return len(s) == 8 and all(isIPv6_part(i) for i in s)

        def isIPv6_part(s):
            if len(s) > 4: return False
            try: return int(s, 16) >= 0 and s[0] != '-'
            except: return False

        if isIPv4(IP): return "IPv4"
        if isIPv6(IP): return "IPv6"
        return "Neither"

    def validIPAddress(self, IP):

        def isIPv4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False

        def isIPv6(s):
            if len(s) > 4: return False
            try: return int(s, 16) >= 0 and s[0] != '-'
            except: return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"
        return "Neither"

############ test case ###########
s=Solution()
print s.validIPAddress("172.16.254.1") #IPv4
print s.validIPAddress("2001:0db8:85a3:033:0:8A2E:0370:7334") #"IPv6"
