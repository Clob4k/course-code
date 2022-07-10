class Solution:
    def longestCommonPrefix(self, strs):
        self.strs = strs
        object = strs[0]
        found = False
        if len(strs) == 1:
            return strs[0]
        for i in range(len(object)):
            slice = object[0:len(strs[0])-i]
            for k in range(1,len(strs)):
                found = False
                slice_len = len(slice)
                compare = strs[k]
                if slice_len > len(compare):
                    break
                if slice == compare[0:slice_len]:
                    found = True
                else:
                    break
            if found:
                return slice
        return ""

ret = Solution().longestCommonPrefix(["reflower","flow","flight"])
print(ret)

# Common prefixes
'''class Solution:
    def longestCommonPrefix(self, strs):
        self.strs = strs
        object = strs[0]
        found = False
        if len(strs) == 1:
            return strs[0]
        for i in range(len(object)):
            for n in range(i+1):
                slice = object[n:n+len(object)-i]
                for k in range(1,len(strs)):
                    found = False
                    slice_len = len(slice)
                    compare = strs[k]
                    if slice_len > len(compare):
                        break
                    for j in range(len(compare)-slice_len+1):
                        clip = compare[j:j+slice_len]
                        if slice == clip:
                            found = True
                    if not found:
                        break
                if found:
                    return slice
        return ""'''
