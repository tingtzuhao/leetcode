class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        scan_len = min([len(word) for word in strs])
        common = ''
        for i in range(scan_len):
            common += strs[0][i]
            for j in range(len(strs)):
                if strs[j][:i+1] == common:
                    next
                else:
                    return common[:i]
        return common