


strs = ["flower","flow","flight"]
class Solution:
    def longestCommonPrefix(self, strs):
        self.strs = strs
        list_of_lists = []
        for i in self.strs:
            word = [j for j in i]
            list_of_lists.append(word)
        print(list_of_lists)

Solution.longestCommonPrefix(strs)