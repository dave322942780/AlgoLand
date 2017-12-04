

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not s:
            if not p:
                return True
            elif p.strip('*') == '':
                return True
        else:
            if p:
                if p[0] == '?':
                    return self.isMatch(s[1:], p[1:])
                elif p[0] == '*':
                    new_p = p.lstrip('*')
                    return self.isMatch(s, new_p) or \
                           self.isMatch(s[1:], '*' + new_p)
                elif p:
                    return s[0] == p[0] and self.isMatch(s[1:], p[1:])
        return False
