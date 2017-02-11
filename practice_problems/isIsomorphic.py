class Solution(object):
    def isIsomorphic(self, c, d):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charMap = {}
        
        for i in range(len(c)):
            if c[i] not in charMap.keys() and d[i] not in charMap.values():
                if c[i] != d[i]:
                    charMap[c[i]] = d[i]
                else:
                    charMap[c[i]] = c[i]

    ## apply transformation
        transformed = []
        for char in c:
            if char in charMap.keys():
		        transformed.append(charMap[char])
            else:
                transformed.append(char)

        if c==d or d == ''.join(transformed):
            return True
        else:
		    return False


c = 'ab'
d = 'ac'

print(isIsomorphic(c,d))