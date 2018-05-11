#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 26/02/2018.


class Solution(object):
    @staticmethod
    def returnStr(stringx):
        cur = 0
        count = 0
        newstr = ""
        for i in range(len(stringx)):
            if stringx[i] == stringx[cur]:
                count += 1
            else:
                if count > 0:
                    newstr += str(count) + stringx[cur]
                count = 1
                cur = i
        if count > 0:
            if count > 0:
                newstr += str(count) + stringx[cur]
        return newstr

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return '0'
        if n == 1:
            return '1'
        else:
            retstr = '1'
            for i in range(1, n):
                retstr = self.returnStr(retstr)
            return retstr


Solution.returnStr("1") == "11"
Solution.returnStr("21") == "1211"

print(Solution.returnStr("1211"))

print(Solution().countAndSay(4))
