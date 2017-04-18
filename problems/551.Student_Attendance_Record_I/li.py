# coding=utf-8
# Author: Jianghan LI
# Question: 551.Student_Attendance_Record_I
# Date: 2017-04-18 13:42- 13:42


class Solution(object):

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and "LLL" not in s
