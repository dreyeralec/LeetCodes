class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ''
        for i in range(len(strs[0])): # have to use first index because len(strs) could = 1
            for s in strs: # check all strings at this index against the first string at strs[0]
                # the prefix answer can only be as long as the shortest string
                # so if the current string we are checking is shorter than the strs[0] then we know
                # we can return whatever we currently have
                # if theres any discrepency at the current index of every string in strs then we know we 
                # found the longest prefix so we can return what we currently have
                if i == len(s) or s[i] != strs[0][i]: 
                    return common
            common += s[i] # all strings have this letter at this index, we can add it to the common prefix
        return common
